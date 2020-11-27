
import pytesseract
from time import sleep
import pyautogui
from keys import *
from win32gui import FindWindow, GetWindowRect
import cv2
import numpy as np
from PIL import Image


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
        self.sort = pyautogui.locateCenterOnScreen("images/sortGold.png", confidence = 0.98, region = self.itemRegion)
        self.searchButton = pyautogui.locateCenterOnScreen("images/search.png", confidence = 0.98, region = self.gameRegion)
        self.next = pyautogui.locateCenterOnScreen("images/nextPage.png", confidence = 0.98, region = self.itemRegion)
        self.mouse = Mouse()
        self.items = []
        self.itemLocations = list(pyautogui.locateAllOnScreen("images/itemPicture.png", confidence = 0.95, region = self.itemRegion))
    def searchSection(self, dictionary, region):
        condense = "images/condense.png"
        for item in dictionary:
            print(item)
            string = f"images/{item}.png"

            center1 = pyautogui.locateCenterOnScreen(string, region = region, confidence = 0.95)

            while not center1:
                pyautogui.moveTo(self.down)
                self.mouse.pressMouse()
                center1 = pyautogui.locateCenterOnScreen(string, region = region, confidence = 0.95)
            pyautogui.moveTo(center1)
            self.mouse.pressMouse()
            subRegion = (region[0] + self.spacing, region[1] , region[2] - self.spacing, region[3])

            if item == "title":
                sleep(1)
                self.mouse.pressMouse()
                self.searchItems()
            elif type(dictionary) is tuple:
                self.searchItems()
            elif dictionary[item]:
                self.searchSection(dictionary[item], subRegion)
            else:
                self.searchItems()


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

        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

        image = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
        image = cv2.blur(image,(5,5))

        string = pytesseract.image_to_string(image, config = '--psm 6')
        string = string.replace("\n", " ")

        return string

    def findItemName(self, image):

        horizontalSpace = 7

        itemPicture = pyautogui.locateOnScreen(image, confidence = 0.97, region = self.gameRegion)
        top = pyautogui.locateOnScreen("images/itemBoxTop.png", confidence = 0.99, region = self.gameRegion)
        divider = pyautogui.locateOnScreen("images/itemBoxDivider.png", confidence = 0.99, region = self.gameRegion)

        x = itemPicture[0] + itemPicture[2] + horizontalSpace
        itemNameRegion = (x, top[1] + 2, top[0] + top[2] - x - 1, divider[1] - top[1] - 2)
        name = self.processImg(pyautogui.screenshot('test.png', region = itemNameRegion))
        return name

    def searchItems(self):
        pyautogui.moveTo(self.searchButton)
        self.mouse.pressMouse()
        pyautogui.moveTo(self.sort)
        self.mouse.pressMouse()

        sleep(2)
        while True:
            self.goldWindows = list(pyautogui.locateAllOnScreen("images/gold.png", confidence = 0.6, region = self.itemRegion))
            print(len(self.itemLocations))
            print(len(self.goldWindows))
            for item in self.itemLocations:

                img = pyautogui.screenshot(region = item)
                if pyautogui.locateOnScreen("images/itemPicture.png", region = item, confidence = 0.95):
                    print("empty")
                    return
                image = pyautogui.screenshot(region = item)
                pyautogui.moveTo(pyautogui.center(item))


                sleep(2)
                print(self.findItemName(image))
                pyautogui.moveTo(self.reset)

                sleep(2)




    def main(self):
        self.searchSection(self.dictionary, self.navRegion)
