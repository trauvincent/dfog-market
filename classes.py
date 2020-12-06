
import pytesseract
from time import sleep
import pyautogui
from keys import *
from win32gui import FindWindow, GetWindowRect
import cv2
import numpy as np

import re
from datetime import datetime

itemNumber = 0
costNumber = 0

class Mouse:
    def __init__(self):
        self.keys = Keys()

    def pressMouse(self):
        self.keys.directMouse(buttons=self.keys.mouse_lb_press)
        sleep(0.1)
        self.keys.directMouse(buttons=self.keys.mouse_lb_release)
        sleep(1)



class Item:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

class AuctionHall:
    spacing = 20
    def __init__(self,dictionary):


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
        self.sort = pyautogui.locateCenterOnScreen("images/name.png", confidence = 0.98, region = self.itemRegion)
        self.searchButton = pyautogui.locateCenterOnScreen("images/search.png", confidence = 0.98, region = self.gameRegion)

        self.mouse = Mouse()
        self.items = []
        self.itemLocations = list(pyautogui.locateAllOnScreen("images/itemPicture.png", confidence = 0.95, region = self.itemRegion))
    def searchSection(self, dictionary, region, tags = []):
        condense = "images/condense.png"
        for item in dictionary:

            print(item)
            string = f"images/{item}.png"
            tags.append(item)

            center1 = pyautogui.locateCenterOnScreen(string, region = region, confidence = 0.95)

            while not center1:
                pyautogui.moveTo(self.down)
                self.mouse.pressMouse()
                center1 = pyautogui.locateCenterOnScreen(string, region = region, confidence = 0.95)
            pyautogui.moveTo(center1)
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
            pyautogui.moveTo(self.up)
            self.mouse.pressMouse()
            onScreen2 = pyautogui.locateCenterOnScreen(condense, region = region, confidence = 0.95)
        pyautogui.moveTo(onScreen2)
        self.mouse.pressMouse()
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


        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        retval, image = cv2.threshold(image,64,255,cv2.THRESH_BINARY)
        image = cv2.resize(image, None, fx=2, fy=2)
        #image = cv2.blur(image,(2,2))
        #image = cv2.bitwise_and(image, image, mask= mask)


        #image = cv2.GaussianBlur(image,(3,3),0)


        string = pytesseract.image_to_string(image, config = '--psm 6')
        string = string.replace("\n", " ")
        if re.search(r"^\+\d+[(\d*)]*\s", string):
            string = re.sub(r"^\+\d+[(\d*)]*\s", "", string)

        if re.search(r"\s\[.*", string):
            string = re.sub(r"\s\[.*", "", string)
        string = string.strip()



        return string
    def makeMask(self, img):
        img_hsv = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2HSV)
        lower = np.array([0,0,0])
        upper = np.array([180,255,40])
        mask = cv2.inRange(img_hsv, lower, upper)
        mask = 255 - mask
        return mask

    def trainTessItem(self):
        global itemNumber
        spacing = 1
        top = pyautogui.locateOnScreen("images/itemBoxTop1.png", region = self.gameRegion)
        divider = pyautogui.locateOnScreen("images/itemBoxDivider1.png", region = self.gameRegion)
        itemNameRegion = (top[0], top[1], top[2], divider[1]-top[1])
        itemName = pyautogui.screenshot(region = itemNameRegion)
        image = cv2.cvtColor(np.array(itemName), cv2.COLOR_RGB2GRAY)
        retval, image = cv2.threshold(image,64,255,cv2.THRESH_BINARY)
        cv2.imwrite(f"images/test/item{itemNumber}.png", image)
        itemNumber += 1
    def trainTessCost(self, cost):
        global costNumber
        gold = pyautogui.locateOnScreen("images/gold.png", region = cost, confidence = 0.5)


        itemName = pyautogui.screenshot(region = gold)
        image = cv2.cvtColor(np.array(itemName), cv2.COLOR_RGB2GRAY)
        retval, image = cv2.threshold(image,64,255,cv2.THRESH_BINARY)
        cv2.imwrite(f"images/test/cost{costNumber}.png", image)
        costNumber += 1
    def processCost(self, img):


        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
        retval, img = cv2.threshold(img,64,255,cv2.THRESH_BINARY)


        #mask = self.makeMask(img)



        #img = cv2.bitwise_and(img, img, mask= mask)



        img = cv2.resize(img, None, fx=2, fy=2)
        #img = cv2.blur(img, (2,2))






        string = pytesseract.image_to_string(img, config = '--psm 6')
        string = string.strip()

        #string = re.sub(r"\D+","",string)
        #string = int(string)

        return string
        #return int(re.search(r'\d+', string)[0])

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




    def findItemName(self, image):



        global itemNumber

        horizontalSpace = 5

        itemPicture = pyautogui.locateOnScreen(image, confidence = 0.95, region = self.gameRegion)
        top = pyautogui.locateOnScreen("images/itemBoxTop.png", region = self.gameRegion)
        dividerRegion = (top[0], top[1], top[2], self.gameRegion[3]-top[1])
        divider = pyautogui.locateOnScreen("images/itemBoxDivider.png", region = dividerRegion)

        x = itemPicture[0] + itemPicture[2] + horizontalSpace
        itemNameRegion = (x, top[1], top[0] + top[2] - x, divider[1] - top[1])


        itemName = pyautogui.screenshot(region = itemNameRegion)
        name = self.processImg(itemName)

        image = cv2.cvtColor(np.array(itemName), cv2.COLOR_RGB2GRAY)
        retval, image = cv2.threshold(image,64,255,cv2.THRESH_BINARY)
        cv2.imwrite(f"images/test/item{itemNumber}.png", image)
        itemNumber += 1

        return name

    def findCost(self, region):
        image = pyautogui.screenshot(region = region)
        cost = self.processCost(image)
        return cost

    def searchItems(self, tags):
        pyautogui.moveTo(self.searchButton)
        self.mouse.pressMouse()
        sleep(5)
        previousItem = None
        pyautogui.moveTo(self.sort)
        dictionary = {}
        self.mouse.pressMouse()
        sleep(2)
        pyautogui.moveTo(self.reset)
        print(tags)
        name = ""

        while True:
            self.goldWindows = list(pyautogui.locateAllOnScreen("images/gold.png", confidence = 0.5, region = self.itemRegion))

            for item, cost in zip(self.itemLocations,self.goldWindows):


                if pyautogui.locateOnScreen("images/itemPicture.png", region = item, confidence = 0.94):
                    print("empty")
                    tags.clear()
                    print(dictionary)

                    return

                image = pyautogui.screenshot(region = item)
                pyautogui.moveTo(pyautogui.center(item))
                sleep(0.1)

                boolean, previousItem = self.itemCheck(previousItem)

                if boolean:
                    #self.trainTessItem()
                    name = self.findItemName(image)




                pyautogui.moveTo(self.reset)
                sleep(0.1)


                if not boolean:
                    dictionary[name]['count'] += 1
                    continue
                price = self.findCost(cost)
                self.trainTessCost(cost)

                print(name)
                print(price)

                if name in dictionary:
                    if price < dictionary[name]['price']:
                        dictionary[name]['price'] = price
                else:
                    dictionary[name] = {'price': price, 'count': 1}



            self.next = pyautogui.locateCenterOnScreen("images/nextPage.png", confidence = 0.98, region = self.itemRegion)
            if self.next:
                pyautogui.moveTo(self.next)
                self.mouse.pressMouse()

            else:
                tags.clear()
                print(dictionary)


                return




    def main(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)
        self.searchSection(self.dictionary, self.navRegion)
