from keys import *
from time import sleep
import cv2
import pyautogui
from collections import deque
from classes import *
from win32gui import FindWindow, GetWindowRect

def main():
    itemlist = ("weapon", "armor", "accessory", "specialEquip", "weaponShape"
        , "recipe", "consumable", "avatar", "cloneAvatar", "emblemAvatar"
        , "cloneEmblem", "emblem", "creature", "profession", "other")
    joblist1 = ("slayer", "fighter", "gunner", "mage", "priest", "thief"
        , "lancer", "agent")
    weaponlist1 = ("shortSword", "katana", "bludgeon", "zanbato", "lightsabre")
    weaponlist2 = ("knuckle", "gauntlets", "claw", "boxingGloves", "tonfa")
    weaponlist3 = ("revolver", "autogun", "musket", "handcannon", "bowgun")
    weaponlist4 = ("spear", "pole", "rod", "staff", "broomstick")
    weaponlist5 = ("cross", "rosary", "totem", "scythe", "battleAxe")
    weaponlist6 = ("dagger", "dualBlade", "wand", "chakra")
    weaponlist7 = ("longLance", "halberd", "beamSpear", "javelin")
    weaponlist8 = ("odachi", "kodachi", "squareSword", "coreBlade")
    armor = ("cloth", "leather", "light", "heavy", "plate")
    partlist1 = ("top", "headshoulder", "bottom", "shoes", "belt")
    accessory = ("necklace", "ring", "bracelet", "title")
    joblist2 = ("slayerdk", "femaleSlayer", "maleFighter", "femaleFighter"
        , "maleGunner", "femaleGunner", "maleMage","femaleMage", "malePriest"
        , "femalePriest", "thief", "knight", "lancer", "agent")
    joblist3 = ("slayerdk", "femaleSlayer", "maleFighter", "femaleFighter"
        , "maleGunner", "femaleGunner", "maleMage2","femaleMage", "malePriest"
        , "femalePriest", "thief", "knight", "lancer", "agent")
    specialEquip = ("subEquip", "magicStone", "earrings")
    joblist4 = ("maleSlayer", "femaleSlayer", "darkKnight", "maleFighter"
        , "femaleFighter", "maleGunner", "femaleGunner", "maleMage2", "femaleMage"
        , "creator", "malePriest", "femalePriest", "thief", "knight", "lancer"
        , "agent")
    recipe = ("weaponRecipe", "armorRecipe", "accessoryRecipe", "specialEquipRecipe")
    consumable = ("package", "consume", "material", "throwInstall", "drawing"
        , "quest", "misc")
    partlist2 = ("hat", "hair", "face", "top", "bottom", "shoes", "torso", "waist"
        , "skin")
    partlist3 = partlist2[:-1]
    emblem = ("red", "yellow", "green", "blue", "platinum", "multi")
    multilist = ("redGreen", "yellowBlue", "threeColors")
    creature = ("pet", "redArtifact", "blueArtifact", "greenArtifact")
    profession = ("alchemist", "animator", "enchanter", "material")
    emptylist = ()

    weapons = (weaponlist1, weaponlist2, weaponlist3, weaponlist4, weaponlist5
        , weaponlist6, weaponlist7, weaponlist8)

    jobWeapon = dict(zip(joblist1, weapons))
    armorParts = {a:partlist1 for a in armor}
    accessoryJob = {a:(joblist2 if a == "title" else ()) for a in accessory}
    specialJob = {a:(joblist4 if a != "earrings" else ()) for a in specialEquip}
    jobShape = {a:b for a,b in zip(joblist1, weapons)}
    recipeJob = {a:b for a,b in zip(recipe, [joblist1, armor, accessory[:-1]
        , specialEquip[:-1]])}
    consumableJob = {a:(joblist2 if a == "package" else ()) for a in consumable}
    jobPart = {a:partlist2 for a in joblist3}
    jobPart2 = {a:partlist3 for a in joblist3}
    colorType = {a:b for a,b in zip(emblem,[(),(),(),(),joblist4,multilist])}
    creatures = {a:() for a in creature}
    professions = {a:() for a in profession}
    emptyDictionary = {}

    

    listOfDictionaries = (jobWeapon, armorParts, accessoryJob, specialJob, jobShape
        , recipeJob, consumableJob, jobPart, jobPart, jobPart2, jobPart2, colorType
        , creatures, professions, emptyDictionary)



    dictQueue = deque(listOfDictionaries)
    dictionary = {a:dictQueue.popleft() for a in itemlist}
    print(dictionary)



    sleep(5)
    auctionHall = AuctionHall(dictionary)
    #print(pyautogui.position())
    #print(vars(auctionHall))

    auctionHall.main()







if __name__ == '__main__':

    main()
