from keys import *
import time
import cv2
import pyautogui
from collections import deque
from classes import *
from win32gui import FindWindow, GetWindowRect










def main():
    time.sleep(5)
    im2 = pyautogui.screenshot('my_screenshot2.png')
    x = pyautogui.locateAllOnScreen('images/itemPicture.png',confidence = 0.95)
    print(pyautogui.position())
    x = list(x)
    print(len(x))
    print(list(x))

    """

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
    joblist20 = ["slayerdk", "femaleSlayer", "maleFighter", "femaleFighter"
        , "maleGunner", "femaleGunner", "maleMage2","femaleMage", "malePriest"
        , "femalePriest", "thief", "knight", "lancer", "agent"]
    specialEquip = ["subEquip", "magicStone", "earrings"]
    joblist3 = ["maleSlayer", "femaleSlayer", "darkKnight", "maleFighter"
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


    list = [joblist1, armor, accessory, specialEquip, joblist1, recipe, consumable
        , joblist20, joblist20, joblist20, joblist20, emblem, creature, profession]
    listQueue = deque(list)


    weapons = [weaponlist1, weaponlist2, weaponlist3, weaponlist4, weaponlist5
        , weaponlist6, weaponlist7, weaponlist8]




    dictionary = {a:([] if a == "other" else listQueue.popleft()) for a in itemlist}
    jobWeapon = dict(zip(joblist1, weapons))
    armorParts = {a:partlist1 for a in armor}
    accessoryJob = {a:(joblist2 if a == "title" else []) for a in accessory}
    specialJob = {a:(joblist3 if a != "earrings" else []) for a in specialEquip}
    jobShape = {a:b for a,b in zip(joblist1, weapons)}
    recipeJob = {a:b for a,b in zip(recipe, [joblist1, armor, accessory[:-1]
        , specialEquip[:-1]])}
    consumableJob = {a:(joblist2 if a == "package" else []) for a in consumable}
    jobPart = {a:partlist2 for a in joblist20}
    jobPart2 = {a:partlist3 for a in joblist20}
    colorType = {a:b for a,b in zip(emblem,[[],[],[],[],joblist3,multilist])}
    creatures = {a:[] for a in creature}
    professions = {a:[] for a in profession}

    listOfDictionaries = [jobWeapon, armorParts, accessoryJob, specialJob, jobShape
        , recipeJob, consumableJob, jobPart, jobPart, jobPart2, jobPart2, colorType
        , creatures, professions]
    dictQueue = deque(listOfDictionaries)

    time.sleep(5)
    gameRegion = Region(gameWindow())
    navRegion = Region(pyautogui.locateOnScreen("images/navigation.png", confidence = 0.98))
    subNavRegion = Region((navRegion.left+20,navRegion.top, navRegion.width, navRegion.height))


    print(dictionary)
    time.sleep(5)
    downLocation = pyautogui.locateCenterOnScreen("images/down.png", confidence = 0.98)
    pyautogui.moveTo(downLocation)
    upLocation = pyautogui.locateCenterOnScreen("images/up.png", confidence = 0.98)
    pyautogui.moveTo(upLocation)
    time.sleep(1)
    resetLocation = pyautogui.locateCenterOnScreen("images/reset.png", confidence = 0.98)
    pyautogui.moveTo(resetLocation)
    pressMouse()
    for a in dictionary:
        print(a)
        string = f"images/{a}.png"
        location1 = pyautogui.locateCenterOnScreen(string,confidence = 0.98, region = navRegion.region)
        pyautogui.moveTo(location1)
        pressMouse()
        time.sleep(1)
        if dictQueue:
            list = dictQueue.popleft()
        else:
            list = {}
        for b in dictionary[a]:
            print(b)
            string2 = f"images/{b}.png"
            location2 = pyautogui.locateCenterOnScreen(string2,confidence = 0.98, region=subNavRegion.region)
            while location2 is None:
                pyautogui.moveTo(downLocation)
                pressMouse()
                time.sleep(1)
                pyautogui.moveTo(resetLocation)
                location2 = pyautogui.locateCenterOnScreen(string2,confidence = 0.98,region = subNavRegion.region)
            pyautogui.moveTo(location2)
            pressMouse()
            time.sleep(1)

            for c in list[b]:
                print(c)
                string3 = f"images/{c}.png"
                location3 = pyautogui.locateCenterOnScreen(string3,confidence = 0.98,region=subNavRegion.region)
                while location3 is None:
                    pyautogui.moveTo(downLocation)
                    pressMouse()
                    time.sleep(1)

                    pyautogui.moveTo(resetLocation)
                    location3 = pyautogui.locateCenterOnScreen(string3,confidence = 0.98,region=subNavRegion.region)
                pyautogui.moveTo(location3)
                pressMouse()
                time.sleep(1.5)

            location2 = pyautogui.locateCenterOnScreen("images/condense.png",confidence = 0.98, region=subNavRegion.region)

            time.sleep(1)
            pyautogui.moveTo(location2)
            pressMouse()
            time.sleep(1)
        location1 = pyautogui.locateCenterOnScreen("images/condense.png",confidence = 0.98, region = navRegion.region)
        while location1 is None and a != "other":
            pyautogui.moveTo(upLocation)
            pressMouse()
            time.sleep(1)

            pyautogui.moveTo(resetLocation)
            location1 = pyautogui.locateCenterOnScreen("images/condense.png",confidence = 0.98,region=navRegion.region)
        pyautogui.moveTo(location1)
        pressMouse()
        time.sleep(1)
        print("done")

    """

    """
   #coordinate of first item in auction hall
   itemX = 180
   itemY = 135

   #change in y to iterate to next item
   itemStepY = 38

   #find image in tabs
   #pyautogui.locateOnScreen('someButton', region=(40, 125, 90, 335))
   time.sleep(5)

   #find search button
   pyautogui.screenshot('my_screenshot')
   #pyautogui.locateOnScreen('someButton', region=(560, 75, 50, 35))
   itemLists = ["weapon.jpg", 'armor.jpg', 'accessory.jpg', "specialEquip.jpg", "weaponShape.jpg", "recipe.jpg",
                "consumable.jpg", "avatar.jpg", "cloneAvatar.jpg", "emblemAvatar.jpg", "cloneEmblem.jpg", "emblem.jpg",
                "creature.jpg", "profession.jpg", "misc.jpg" ]


   pyautogui.moveTo(200, 200)

   for items in itemLists:

      x, y = pyautogui.locateCenterOnScreen(items, confidence = 0.85)
      keys = Keys()


      time.sleep(1)
      print(x)
      print(y)
      pyautogui.moveTo(x, y)

      keys.directMouse(buttons=keys.mouse_lb_press)
      time.sleep(0.5)
      keys.directMouse(buttons=keys.mouse_lb_release)
      time.sleep(0.5)
      keys.directMouse(buttons=keys.mouse_lb_press)
      time.sleep(0.5)
      keys.directMouse(buttons=keys.mouse_lb_release)
      time.sleep(0.5)
      x, y = pyautogui.locateCenterOnScreen("search.jpg", confidence = 0.85)
      pyautogui.moveTo(x, y)

      keys.directMouse(buttons=keys.mouse_lb_press)
      time.sleep(0.5)
      keys.directMouse(buttons=keys.mouse_lb_release)
      time.sleep(0.5)

      """
      #click, delay, click button to show items


   # show the output images
def gameWindow():

    gameHandle = FindWindow(None, "Dungeon Fighter Online")
    gameWindow = GetWindowRect(gameHandle)
    gameBox = (gameWindow[0], gameWindow[1], gameWindow[2]-gameWindow[0], gameWindow[3]-gameWindow[1])

    return gameBox
def pressMouse():
    keys = Keys()
    keys.directMouse(buttons=keys.mouse_lb_press)
    time.sleep(0.1)
    keys.directMouse(buttons=keys.mouse_lb_release)
    time.sleep(0.1)

if __name__ == '__main__':

    main()
