

import random
import pytesseract
from time import sleep
import pyautogui
from keys import *
from win32gui import FindWindow, GetWindowRect
import cv2
import numpy as np
import glob
import os

import re
from datetime import datetime

number = len(glob.glob1("images/test","*.png"))

items = []
costs = []


strings = []

def readData(location):
    list = []
    files = os.listdir(f"images/test/{location}")
    for file in files:
        string = f"images/test/{location}/{file}"
        if file.endswith('.txt'):
            with open(string) as f:
                text = f.read()
                list.append((text, file))

    print(*list,  sep="\n")


def transcribeData():
    files = os.listdir("images/test")
    list = []
    string = ""
    for file in files:
        if file.endswith('.png'):
            string = pytesseract.image_to_string(f'images/test/{file}', config = '--psm 6')
            string = string.strip()
            if file.startswith('cost'):
                string = string.replace(".",",")
                string = re.sub(r"^Total\s|Total,", "Total.", string)
                string = re.sub("Gald", "Gold", string)
                string = re.sub("=", "", string)

            file = file.replace(".png",".gt.txt")
            with open(os.path.join("images/test", file), "w+") as f:
                f.write(string)
                f.close()
def editData(old, new):
    files = os.listdir("images/test")
    list = []
    words = []
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join("images/test", file)) as f:
                text = f.read()
                if old in text:
                    text = text.replace(old, new)
                    list.append(file)
                    words.append(text)
    for file, word in zip(list, words):
        with open(os.path.join("images/test", file), "w+") as f:
            f.write(word)
            f.close()

def cleanData(location):
    list = []
    files = os.listdir(f"images/test/{location}")
    delete = []
    for file in files:
        string = f"images/test/{location}/{file}"
        if file.endswith('.txt'):
            with open(string) as f:
                text = f.read()
                if text not in list:
                    list.append(text)
                else:
                    delete.append(file)
    for file in delete:
        string = f"images/test/{location}/{file}"
        os.remove(string)
        string = string.replace(".gt.txt", ".png")
        os.remove(string)
    number = 0
    files = os.listdir(f"images/test/{location}")
    for file in files:
        if file.endswith('.txt'):
            string = f"images/test/{location}/{file}"

            string1 = re.sub("s\d+", str(number), string)

            os.rename(string, string1)
            string = string.replace(".gt.txt", ".png")
            string1 = string1.replace(".gt.txt", ".png")
            os.rename(string, string1)
            number += 1















class Mouse:
    def __init__(self):
        self.keys = Keys()

    def pressMouse(self):
        self.keys.directMouse(buttons=self.keys.mouse_lb_press)
        sleep(0.1)
        self.keys.directMouse(buttons=self.keys.mouse_lb_release)
        sleep(1)

    def moveMouse(self, location):
        pyautogui.moveTo(location)

    def moveRandom(self):
        x, y = pyautogui.size()
        randomX = random.randint(0, x - 1)
        randomY = random.randint(0, y - 1)
        location = (randomX, randomY)
        pyautogui.moveTo(location)

class Image:
    def __init__(self, image):
        self.image = image

    def gray(self):
        self.image = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2GRAY)

    def threshold(self):
        retval, self.image = cv2.threshold(self.image,64,255,cv2.THRESH_BINARY)

    def resize(self, factor, interpolate = cv2.INTER_LINEAR):
        self.image = cv2.resize(self.image, None, fx=factor, fy=factor, interpolation = interpolate)

    def imageToString(self, language = "eng"):
        self.string = pytesseract.image_to_string(self.image, config = '--psm 6', lang=language)

    def blur(self, factor):
        self.image = cv2.blur(self.image, (2,2))


    def removeEmptySpace(self):
        borderSize = 10

        coords = cv2.findNonZero(self.image)
        x, y, w, h = cv2.boundingRect(coords)
        self.image = self.image[y : y + h , x  : x + w ]

    def addBlackBorder(self, borderSize = 10):
        self.image = cv2.copyMakeBorder(self.image, borderSize, borderSize, borderSize, borderSize, cv2.BORDER_CONSTANT)



class Item:
    def __init__(self, name, price, count, tags):
        self.name = name
        self.price = price
        self.count = count
        self.tags = tags

class AuctionHall:
    spacing = 20
    def __init__(self,dictionary):
        self.testItems = self.testData("item")
        self.testCosts = self.testData("cost")

        self.dictionary = dictionary
        self.gameRegion = self.getGameRegion()
        self.navRegion = pyautogui.locateOnScreen("images/navigation.png", confidence = 0.95)
        self.subNavRegion = (self.navRegion[0] + self.spacing, self.navRegion[1]
            , self.navRegion[2], self.navRegion[3])
        self.itemTypeRegion = self.subNavRegion
        self.itemRegion = pyautogui.locateOnScreen("images/itemRegion.png", confidence = 0.9)

        self.up = pyautogui.locateCenterOnScreen("images/up.png", confidence = 0.98, region = self.navRegion)
        self.down = pyautogui.locateCenterOnScreen("images/down.png", confidence = 0.98, region = self.navRegion)
        self.reset = pyautogui.locateCenterOnScreen("images/reset.png", confidence = 0.98, region = self.gameRegion)

        self.sortArea = pyautogui.locateOnScreen("images/name.png", confidence = 0.95, region = self.itemRegion)
        self.sort = pyautogui.center(self.sortArea)
        self.searchButton = pyautogui.locateCenterOnScreen("images/search.png", confidence = 0.98, region = self.gameRegion)

        self.mouse = Mouse()
        self.items = []
        self.itemLocations = list(pyautogui.locateAllOnScreen("images/itemPicture.png", confidence = 0.95, region = self.itemRegion))

    def testData(self, location):
        list = []
        files = os.listdir(f"images/test/{location}")
        for file in files:
            if file.endswith('.txt'):
                with open(f"images/test/{location}" + f"/{file}") as f:
                    text = f.read()
                    list.append(text)


        return list
    def searchSection(self, dictionary, region, tags = []):
        condense = "images/condense.png"
        for item in dictionary:

            print(item)
            string = f"images/{item}.png"
            tags.append(item)

            center1 = pyautogui.locateCenterOnScreen(string, region = region, confidence = 0.95)

            while not center1:
                self.mouse.moveMouse(self.down)
                self.mouse.pressMouse()
                center1 = pyautogui.locateCenterOnScreen(string, region = region, confidence = 0.95)
            self.mouse.moveMouse(center1)
            self.mouse.pressMouse()
            subRegion = (region[0] + self.spacing, region[1] , region[2] - self.spacing, region[3])

            if item == "title":

                self.mouse.pressMouse()
                self.searchItems(tags)
            elif type(dictionary) is tuple:
                self.searchItems(tags)
            elif dictionary[item]:
                self.searchSection(dictionary[item], subRegion, tags)
            else:
                self.searchItems(tags)


        region = (region[0] - self.spacing, region[1], region[2] + self.spacing, region[3])
        onScreen2 = pyautogui.locateOnScreen(condense, region = region, confidence = 0.95)

        while not onScreen2 and dictionary[item]:
            self.mouse.moveMouse(self.up)
            self.mouse.pressMouse()
            onScreen2 = pyautogui.locateCenterOnScreen(condense, region = region, confidence = 0.95)
        self.mouse.moveMouse(onScreen2)
        self.mouse.pressMouse()
        tags.pop()
    def getGameRegion(self):
        gameHandle = FindWindow(None, "Dungeon Fighter Online")
        try:
            gameWindow = GetWindowRect(gameHandle)
            game = (gameWindow[0], gameWindow[1], gameWindow[2]-gameWindow[0], gameWindow[3]-gameWindow[1])
        except:
            game = None
        return game
    def processImg(self, image):


        #mask = self.makeMask(image)
        global itemNumber

        global items
        image.gray()
        image.threshold()
        image.resize(3, cv2.INTER_LANCZOS4)
        #image = cv2.blur(image,(2,2))
        #image = cv2.bitwise_and(image, image, mask= mask)



        #image = cv2.GaussianBlur(image,(3,3),0)
        image.removeEmptySpace()
        image.addBlackBorder()
        image.imageToString("eng")


        string = image.string.strip()

        if "\n" not in string and string not in self.testItems:
            length = len(self.testItems)
            cv2.imwrite(f"images/test/item/item{length}.png", image.image)
            with open(f"images/test/item/item{length}.gt.txt", "w+") as f:   # Opens file and casts as f
                f.write(string)

            self.testItems.append(string)

        string = string.replace("\n", " ")
        """
        if re.search(r"^\+\d+[(\d*)]*\s", string):
            string = re.sub(r"^\+\d+[(\d*)]*\s", "", string)
        """
        """
        if re.search(r"\s\[.*", string):
            string = re.sub(r"\s\[.*", "", string)
        """




        return string
    def makeMask(self, img):
        img_hsv = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2HSV)
        lower = np.array([0,0,0])
        upper = np.array([180,255,40])
        mask = cv2.inRange(img_hsv, lower, upper)
        mask = 255 - mask
        return mask



    def processCost(self, img):
        global items
        global number

        global costNumber


        #mask = self.makeMask(img)



        #img = cv2.bitwise_and(img, img, mask= mask)


        img.gray()
        img.threshold()
        img.resize(3, cv2.INTER_LANCZOS4)
        #img.blur(2)





        #image = cv2.GaussianBlur(image,(3,3),0)


        img.removeEmptySpace()
        img.addBlackBorder()
        img.imageToString("eng")




        string = img.string.strip()
        string = string.replace(".",",")
        string = re.sub(r"^Total\s|Total,", "Total.", string)

        string = re.sub("Gald", "Gold", string)
        string = re.sub("=", "", string)

        if string not in self.testCosts:
            length = len(self.testCosts)
            cv2.imwrite(f"images/test/cost/cost{length}.png", img.image)
            with open(f"images/test/cost/cost{length}.gt.txt", "w+") as f:
                f.write(string)
            self.testCosts.append(string)





        #string = re.sub(r"\D+","",string)
        #string = int(string)

        return string
        #return int(re.search(r'\d+', string)[0])
    """
    def itemCheck(self, image):
        top = pyautogui.locateOnScreen("images/itemBoxTop.png", region = self.gameRegion)
        divider = pyautogui.locateOnScreen("images/itemBoxDivider.png", region = self.gameRegion)

        itemRegion = (top[0], top[1], top[2], divider[1] - top[1])

        try:
            region = pyautogui.locateOnScreen(image, region = itemRegion, confidence = 0.9)
            if region is None:
                return True, pyautogui.screenshot(region = itemRegion)
            else:
                return False, image

        except:
            return True, pyautogui.screenshot(region = itemRegion)
    """



    def findItemName(self, image, checkForImage, useNameField):



        #global itemNumber



        if useNameField:
            self.mouse.moveMouse(self.reset)
            sleep(0.2)
            itemNameRegion = (self.sortArea[0], useNameField[1], self.sortArea[2], useNameField[3])
        else:

            sleep(0.2)
            horizontalSpace = 5
            top = pyautogui.locateOnScreen("images/itemBoxTop.png", region = self.gameRegion)
            dividerRegion = (top[0], top[1], top[2], self.gameRegion[3]-top[1])
            divider = pyautogui.locateOnScreen("images/itemBoxDivider.png", region = dividerRegion)

            if checkForImage:
                itemPicture = pyautogui.locateOnScreen(image, confidence = 0.5, region = dividerRegion)
                x = itemPicture[0] + itemPicture[2] + horizontalSpace
                itemNameRegion = (x, top[1], top[0] + top[2] - x, divider[1] - top[1])
            else:
                itemNameRegion = (top[0], top[1], top[2], divider[1] - top[1])


        itemName = Image(pyautogui.screenshot(region = itemNameRegion))
        name = self.processImg(itemName)


        return name

    def findCost(self, region):
         total = pyautogui.locateOnScreen("images/total.png", region = region, confidence = 0.98)
         gold = pyautogui.locateOnScreen("images/gold.png", region = region, confidence = 0.98)
         region = (total[0] + total[2], total[1], gold[0] - total[0] - total[2], total[3])
         image = Image(pyautogui.screenshot(region = region))
         cost = self.processCost(image)
         return cost

    def searchItems(self, tags):
        self.mouse.moveMouse(self.searchButton)
        self.mouse.pressMouse()
        sleep(5)
        previousItem = None
        checkForImage = True
        useNameField = None
        self.mouse.moveMouse(self.sort)
        dictionary = {}
        self.mouse.pressMouse()
        sleep(2)
        self.mouse.moveMouse(self.reset)
        print(tags)
        sleep(0.2)
        name = ""

        while True:
            self.goldWindows = list(pyautogui.locateAllOnScreen("images/cost.png", confidence = 0.5, region = self.itemRegion))

            for item, cost in zip(self.itemLocations,self.goldWindows):


                if pyautogui.locateOnScreen("images/itemPicture.png", region = item, confidence = 0.94):
                    print("empty")
                    tags.pop()
                    print(dictionary)

                    return
                if tags[0] in ['avatar', 'cloneAvatar', 'emblemAvatar', 'cloneEmblem'] or tags[1] in ['pet']:
                    checkForImage = False
                if tags[0] in ['cloneEmblem', 'emblemAvatar'] or tags[1] in ['material']:
                    useNameField = item

                image = pyautogui.screenshot(region = item)
                self.mouse.moveRandom()

                self.mouse.moveMouse(pyautogui.center(item))



                    #self.trainTessItem()

                name = self.findItemName(image, checkForImage, useNameField)




                self.mouse.moveMouse(self.reset)

                price = self.findCost(cost)



                #self.trainTessCost(cost)

                print(name)
                print(price)

                if name in dictionary:
                    dictionary[name]['count'] += 1
                    if price < dictionary[name]['price']:
                        dictionary[name]['price'] = price
                else:
                    dictionary[name] = {'price': price, 'count': 1}
            self.next = pyautogui.locateCenterOnScreen("images/nextPage.png", confidence = 0.98, region = self.itemRegion)
            if self.next:
                self.mouse.moveMouse(self.next)
                self.mouse.pressMouse()
                sleep(0.2)
            else:
                tags.pop()
                print(dictionary)
                return


    def main(self):
        print("start edit")
        #editData("..","...")
    #    transcribeData()
        #cleanData("cost")
        print("end edit")
        #readData("item")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)

        self.searchSection(self.dictionary, self.navRegion)
