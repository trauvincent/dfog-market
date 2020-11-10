from keys import *
import time
import cv2
import pyautogui









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
    specialEquip = ["subEquip", "magicStone", "earrings"]
    joblist3 = ["maleSlayer", "femaleSlayer", "darkKnight", "maleFighter"
        , "femaleFighter", "maleGunner", "femaleGunner", "maleMage", "femaleMage"
        , "creator", "malePriest", "femalePriest", "thief", "knight", "lancer"
        , "agent"]
    recipe = ["weaponRecipe", "armorRecipe", "accessoryRecipe", "specialEquipRecipe"]
    consumable = ["package", "consume", "material", "throwInstall", "drawing"
        , "quest", "misc"]
    partlist2 = ["hat", "hair", "face", "top", "bottom", "shoes", "torso", "waist"
        , "skin"]
    emblem = ["red", "yellow", "green", "blue", "platinum", "multi"]
    multilist = ["redGreen", "yellowBlue", "threeColors"]
    creature = ["pet", "redArtifact", "blueArtifact", "greenArtifact"]
    profession = ["alchemist", "animator", "enchanter", "material"]

    list = [joblist1, armor, accessory, specialEquip, joblist1, recipe, consumable
        , joblist2, joblist2, joblist2, joblist2, emblem, creature, profession]
    weapons = [weaponlist1, weaponlist2, weaponlist3, weaponlist4, weaponlist5
        , weaponlist6, weaponlist7, weaponlist8]


    dictionary = dict(zip(itemlist, list))
    jobWeapon = dict(zip(joblist1, weapons))
    armorParts = {a:partlist1 for a in armor}
    accessoryJob = {a:joblist2 for a in accessory if a == "title"}
    specialJob = {a:joblist3 for a in specialEquip if a != "earrings"}
    jobShape = {a:b for a,b in zip(joblist1, weapons)}
    recipeJob = {a:b for a,b in zip(recipe, [joblist1, armor, accessory[:-1]
        , specialEquip[:-1]])}
    consumableJob = {a:joblist2 for a in consumable if a == "package"}
    jobPart = {a:partlist2 for a in joblist2}
    colorType = {a:b for a,b in zip(emblem[-2:],[joblist3,multilist])}

    listOfDictionaries = [jobWeapon, armorParts, accessoryJob, specialJob, jobShape
        , recipeJob, consumableJob, jobPart, colorType]


    print(dictionary)
    time.sleep(5)
    for key in dictionary:
        print(key)
        string = f"images/{key}.png"
        location = pyautogui.locateCenterOnScreen(string,confidence = 0.9)
        pyautogui.moveTo(location)

        pressMouse()
        time.sleep(1)
        for item in dictionary[key]:
            print(item)
            string2 = f"images/{item}.png"
            location2 = pyautogui.locateCenterOnScreen(string2,confidence = 0.9)
            pyautogui.moveTo(location2)
            pressMouse()
            time.sleep(1)
            pressMouse()
        pyautogui.moveTo(location)
        pressMouse()

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

def pressMouse():
    keys = Keys()
    keys.directMouse(buttons=keys.mouse_lb_press)
    time.sleep(0.1)
    keys.directMouse(buttons=keys.mouse_lb_release)
    time.sleep(1)

if __name__ == '__main__':

    main()
