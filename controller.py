from keys import *
from time import sleep
import cv2
import pyautogui
from collections import deque
from classes import *
from win32gui import FindWindow, GetWindowRect










def main():



    itemlist = ["weapon", "armor", "accessory", "specialEquip", "weaponShape"
        , "recipe", "consumable", "avatar", "cloneAvatar", "emblemAvatar"
        , "cloneEmblem", "emblem", "creature", "profession", "other"]

    joblist1 = ["slayer", "fighter", "gunner", "mage", "priest", "thief"
        , "lancer", "agent"]
    weaponlist1 = ["shortSword", "katana", "bludgeon", "zanbato", "lightsabre"]
    weaponlist2 = ["knuckle", "gauntlets", "claw", "boxingGloves", "tonfa"]
    weaponlist3 = ["revolver", "autogun", "musket", "handcannon", "bowgun"]
    weaponlist4 = ["spear", "pole", "rod", "staff", "broomstick"]
    weaponlist5 = ["cross", "rosary", "totem", "scythe", "battleAxe"]
    weaponlist6 = ["dagger", "dualBlade", "wand", "chakra"]
    weaponlist7 = ["longLance", "halberd", "beamSpear", "javelin"]
    weaponlist8 = ["odachi", "kodachi", "squareSword", "coreBlade"]
    armor = ["cloth", "leather", "light", "heavy", "plate"]
    partlist1 = ["top", "headshoulder", "bottom", "shoes", "belt"]
    accessory = ["necklace", "ring", "bracelet", "title"]
    joblist2 = ["slayerdk", "femaleSlayer", "maleFighter", "femaleFighter"
        , "maleGunner", "femaleGunner", "maleMage","femaleMage", "malePriest"
        , "femalePriest", "thief", "knight", "lancer", "agent"]
    joblist3 = ["slayerdk", "femaleSlayer", "maleFighter", "femaleFighter"
        , "maleGunner", "femaleGunner", "maleMage2","femaleMage", "malePriest"
        , "femalePriest", "thief", "knight", "lancer", "agent"]
    specialEquip = ["subEquip", "magicStone", "earrings"]
    joblist4 = ["maleSlayer", "femaleSlayer", "darkKnight", "maleFighter"
        , "femaleFighter", "maleGunner", "femaleGunner", "maleMage2", "femaleMage"
        , "creator", "malePriest", "femalePriest", "thief", "knight", "lancer"
        , "agent"]
    recipe = ["weaponRecipe", "armorRecipe", "accessoryRecipe", "specialEquipRecipe"]
    consumable = ["package", "consume", "material", "throwInstall", "drawing"
        , "quest", "misc"]
    partlist2 = ["hat", "hair", "face", "top", "bottom", "shoes", "torso", "waist"
        , "skin"]
    partlist3 = partlist2[:-1]
    emblem = ["red", "yellow", "green", "blue", "platinum", "multi"]
    multilist = ["redGreen", "yellowBlue", "threeColors"]
    creature = ["pet", "redArtifact", "blueArtifact", "greenArtifact"]
    profession = ["alchemist", "animator", "enchanter", "material"]
    emptylist = []


    weapons = [weaponlist1, weaponlist2, weaponlist3, weaponlist4, weaponlist5
        , weaponlist6, weaponlist7, weaponlist8]
    list = [joblist1, armor, accessory, specialEquip, joblist1, recipe, consumable
        , joblist3, joblist3, joblist3, joblist3, emblem, creature, profession
        , emptylist]
    listQueue = deque(list)



    dictionary = {a:listQueue.popleft() for a in itemlist}
    jobWeapon = dict(zip(joblist1, weapons))
    armorParts = {a:partlist1 for a in armor}
    accessoryJob = {a:(joblist2 if a == "title" else []) for a in accessory}
    specialJob = {a:(joblist4 if a != "earrings" else []) for a in specialEquip}
    jobShape = {a:b for a,b in zip(joblist1, weapons)}
    recipeJob = {a:b for a,b in zip(recipe, [joblist1, armor, accessory[:-1]
        , specialEquip[:-1]])}
    consumableJob = {a:(joblist2 if a == "package" else []) for a in consumable}
    jobPart = {a:partlist2 for a in joblist3}
    jobPart2 = {a:partlist3 for a in joblist3}
    colorType = {a:b for a,b in zip(emblem,[[],[],[],[],joblist4,multilist])}
    creatures = {a:[] for a in creature}
    professions = {a:[] for a in profession}
    emptyDictionary = {}

    listOfDictionaries = [jobWeapon, armorParts, accessoryJob, specialJob, jobShape
        , recipeJob, consumableJob, jobPart, jobPart, jobPart2, jobPart2, colorType
        , creatures, professions, emptyDictionary]
    sleep(5)




    dictQueue = deque(listOfDictionaries)
    gameRegion = Region()
    mouse = Mouse()
    auctionHall = AuctionHall(dictionary, dictQueue)
    auctionHall.search()


    horizontalSpacing = 20
    gameRegion = Region(gameWindow())
    navRegion = Region(pyautogui.locateOnScreen("images/navigation.png", confidence = 0.98))
    subNavRegion = Region((navRegion.left+horizontalSpacing,navRegion.top, navRegion.width, navRegion.height))
    itemNavRegion = Region(subNavRegion.region)

    sleep(5)
    downLocation = pyautogui.locateCenterOnScreen("images/down.png", confidence = 0.98)
    pyautogui.moveTo(downLocation)
    upLocation = pyautogui.locateCenterOnScreen("images/up.png", confidence = 0.98)
    pyautogui.moveTo(upLocation)
    resetLocation = pyautogui.locateCenterOnScreen("images/reset.png", confidence = 0.98)
    pyautogui.moveTo(resetLocation)
    pressMouse()
    pyautogui.position()
    print(upLocation)

    """
    for a in dictionary:
        print(a)
        string = f"images/{a}.png"
        location1 = pyautogui.locateCenterOnScreen(string,confidence = 0.98, region = navRegion.region)
        pyautogui.moveTo(location1)
        pressMouse()
        list = dictQueue.popleft()
        for b in dictionary[a]:
            print(b)
            string2 = f"images/{b}.png"
            location2 = pyautogui.locateOnScreen(string2,confidence = 0.98, region=subNavRegion.region)
            verticalSpacing = location2.height
            top = location2.top
            location2 = pyautogui.center(location2)
            while location2 is None:
                pyautogui.moveTo(downLocation)
                pressMouse()
                pyautogui.moveTo(resetLocation)
                location2 = pyautogui.locateCenterOnScreen(string2,confidence = 0.98,region = subNavRegion.region)
            pyautogui.moveTo(location2)
            pressMouse()
            itemNavRegion.top = top + verticalSpacing
            itemNavRegion.height -= verticalSpacing
            for c in list[b]:
                print(c)
                string3 = f"images/{c}.png"
                location3 = pyautogui.locateCenterOnScreen(string3,confidence = 0.98,region=itemNavRegion.region)
                while location3 is None:
                    pyautogui.moveTo(downLocation)
                    pressMouse()
                    pyautogui.moveTo(resetLocation)
                    location3 = pyautogui.locateCenterOnScreen(string3,confidence = 0.98,region=itemNavRegion.region)
                pyautogui.moveTo(location3)
                pressMouse()
            location2 = pyautogui.locateCenterOnScreen("images/condense.png",confidence = 0.98, region=subNavRegion.region)
            pyautogui.moveTo(location2)
            pressMouse()
        location1 = pyautogui.locateCenterOnScreen("images/condense.png",confidence = 0.98, region = navRegion.region)
        while location1 is None and a != "other":
            pyautogui.moveTo(upLocation)
            pressMouse()
            pyautogui.moveTo(resetLocation)
            location1 = pyautogui.locateCenterOnScreen("images/condense.png",confidence = 0.98,region=navRegion.region)
        pyautogui.moveTo(location1)
        pressMouse()



        """






if __name__ == '__main__':

    main()
