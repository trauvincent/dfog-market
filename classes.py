"""
class Item:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Item.count += 1
class Weapon(Item, Recipe):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Slayer(Weapon, WeaponShape):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class MaleSlayer(Slayer, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class DarkKnight(Platinum, SubEquip, MagicStone):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class FemaleSlayer(Slayer, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Knight(Slayer, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class ShortSword(Slayer):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Katana(Slayer):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Bludgeon(Slayer):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Zanbato(Slayer):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class LightSabre(Slayer):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Fighter(Weapon, WeaponShape):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class MaleFighter(Fighter, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class FemaleFighter(Fighter, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Knuckle(Fighter):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Gauntlets(Fighter):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Claw(Fighter):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class BoxingGloves(Fighter):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Tonfa(Fighter):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Gunner(Weapon, WeaponShape):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class MaleGunner(Gunner, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class FemaleGunner(Gunner, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Revolver(Gunner):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class AutoGun(Gunner):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Musket(Gunner):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class HandCannon(Gunner):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class BowGun(Gunner):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Mage(Weapon, WeaponShape):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class MaleMage(Mage, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class FemaleMage(Mage, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Creator(Platinum, SubEquip, MagicStone):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Spear(Mage):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Pole(Mage):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Rod(Mage):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Staff(Mage):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Broomstick(Mage):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Priest(Weapon, WeaponShape):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class MalePriest(Priest, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class FemalePriest(Priest, Title, SubEquip, MagicStone, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Cross(Priest):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Rosary(Priest):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Totem(Priest):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Scythe(Priest):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class BattleAxe(Priest):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Thief(Weapon, Title, SubEquip, MagicStone, WeaponShape, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Dagger(Thief):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class DualBlade(Thief):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Wand(Thief):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Chakra(Thief):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Lancer(Weapon, Title, SubEquip, MagicStone, WeaponShape, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class LongLance(Lancer):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Halberd(Lancer):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class BeamSpear(Lancer):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Javelin(Lancer):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Agent(Weapon, Title, SubEquip, MagicStone, WeaponShape, Avatar, CloneAvatar, EmblemAvatar, CloneEmblem, Platinum):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Odachi(Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Kodachi(Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class SquareSword(Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class CoreBlade(Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Armor(Item, Recipe):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Cloth(Armor):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Leather(Armor):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Light(Armor):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Heavy(Armor):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Plate(Armor):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Top(Cloth, Leather, Light, Heavy, Plate, MaleSlayer, FemaleSlayer, MaleFighter, FemaleFighter, MaleGunner, FemaleGunner, MaleMage, FemaleMage, MalePriest, FemalePriest, Thief, Knight, Lancer, Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class HeadShoulder(Cloth, Leather, Light, Heavy, Plate):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Bottom(Cloth, Leather, Light, Heavy, Plate, MaleSlayer, FemaleSlayer, MaleFighter, FemaleFighter, MaleGunner, FemaleGunner, MaleMage, FemaleMage, MalePriest, FemalePriest, Thief, Knight, Lancer, Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Shoes(Cloth, Leather, Light, Heavy, Plate, MaleSlayer, FemaleSlayer, MaleFighter, FemaleFighter, MaleGunner, FemaleGunner, MaleMage, FemaleMage, MalePriest, FemalePriest, Thief, Knight, Lancer, Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Belt(Cloth, Leather, Light, Heavy, Plate):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Accessory(Item, Recipe):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Necklace(Accessory):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Ring(Accessory):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Bracelet(Accessory):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Title(Accessory):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class SpecialEquip(Item, Recipe):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class SubEquip(SpecialEquip):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class MagicStone(SpecialEquip):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Earrings(SpecialEquip):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class WeaponShape(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Recipe(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Consumable(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Package(Consumable):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Consume(Consumable):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Material(Consumable):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class ThrowInstall(Consumable):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Drawing(Consumable):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Quest(Consumable):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)


class Avatar(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Hat(MaleSlayer, FemaleSlayer, MaleFighter, FemaleFighter, MaleGunner, FemaleGunner, MaleMage, FemaleMage, MalePriest, FemalePriest, Thief, Knight, Lancer, Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Hair(MaleSlayer, FemaleSlayer, MaleFighter, FemaleFighter, MaleGunner, FemaleGunner, MaleMage, FemaleMage, MalePriest, FemalePriest, Thief, Knight, Lancer, Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Face(MaleSlayer, FemaleSlayer, MaleFighter, FemaleFighter, MaleGunner, FemaleGunner, MaleMage, FemaleMage, MalePriest, FemalePriest, Thief, Knight, Lancer, Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Torso(MaleSlayer, FemaleSlayer, MaleFighter, FemaleFighter, MaleGunner, FemaleGunner, MaleMage, FemaleMage, MalePriest, FemalePriest, Thief, Knight, Lancer, Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Waist(MaleSlayer, FemaleSlayer, MaleFighter, FemaleFighter, MaleGunner, FemaleGunner, MaleMage, FemaleMage, MalePriest, FemalePriest, Thief, Knight, Lancer, Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Skin(MaleSlayer, FemaleSlayer, MaleFighter, FemaleFighter, MaleGunner, FemaleGunner, MaleMage, FemaleMage, MalePriest, FemalePriest, Thief, Knight, Lancer, Agent):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class CloneAvatar(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class EmblemAvatar(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class CloneEmblem(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Emblem(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Red(Emblem):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Yellow(Emblem):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Green(Emblem):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Blue(Emblem):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Platinum(Emblem):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Multi(Emblem):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class RedGreen(Multi):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class YellowBlue(Multi):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class ThreeColors(Multi):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Creature(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Pet(Creature):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class RedArtifact(Creature):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class BlueArtifact(Creature):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class GreenArtifact(Creature):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Profession(Item):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Alchemist(Profession):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)

class Animator(Profession):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Enchanter(Profession):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Material(Profession):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
class Misc(Item, Consumable):
    count = 0
    def __init__(self, name, price):
        super().__init__(name,price)
"""
from time import sleep
import pyautogui
from keys import *
from win32gui import FindWindow, GetWindowRect
import cv2

class AuctionHall:
    def __init__(self, groups, dictQueue):
        self.groups=groups
        self.dictQueue = dictQueue
        self.mouse = Mouse()


    def sortByGold(region):
        pyautogui.locateCenterOnScreen("images/sortByGold.png", region = region)
        self.mouse.pressMouse()
    def search(region):
        pyautogui.locateCenterOnScreen("images/search.png", region = region)
        self.mouse.pressMouse()
    def nextItemPage(region):
        pyautogui.locateCenterOnScreen("images/nextPage.png", region = region)
        self.mouse.pressMouse()
    def search(self):
        sleep(5)
        horizontalSpacing = 20
        gameRegion = Region().gameRegion()
        navRegion = Region(pyautogui.locateOnScreen("images/navigation.png", confidence = 0.98))
        subNavRegion = Region((navRegion.left+horizontalSpacing,navRegion.top, navRegion.width, navRegion.height))
        itemNavRegion = Region(subNavRegion.region)
        print(navRegion.region)
        print(subNavRegion.region)
        condense = "images/condense.png"
        upLocation = pyautogui.locateCenterOnScreen("images/up.png", confidence = 0.98, region = gameRegion)
        downLocation = pyautogui.locateCenterOnScreen("images/down.png", confidence = 0.98, region = gameRegion)

        for group in self.groups:
            print(group)
            string1 = f"images/{group}.png"
            self.mouse.clickCenter(string1, region = navRegion.region)
            itemDictionary = self.dictQueue.popleft()
            for subGroup in self.groups[group]:
                print(subGroup)
                string2 = f"images/{subGroup}.png"
                subNavRegion.findsubRegion(string2)
                top = subNavRegion.topSub
                verticalSpacing = subNavRegion.verticalSpacing
                self.mouse.findLocation(string2, region = subNavRegion.region)
                while self.mouse.location is None:
                    self.mouse.moveClick(downLocation)
                    self.mouse.findLocation(string2, region = subNavRegion.region)
                self.mouse.moveClick(self.mouse.location)
                itemNavRegion.top = top + verticalSpacing
                itemNavRegion.height -= verticalSpacing
                for items in itemDictionary[subGroup]:
                    print(items)
                    string3 = f"images/{items}.png"
                    self.mouse.findLocation(string3, region = itemNavRegion.region)
                    while self.mouse.location is None:
                        self.mouse.moveClick(downLocation)
                        self.mouse.findLocation(string3, region = itemNavRegion.region)
                    self.mouse.moveClick(self.mouse.location)
                self.mouse.clickCenter(condense, region = subNavRegion.region)
            self.mouse.findLocation(condense, region = navRegion.region)
            while self.mouse.location is None and group != "other":
                self.mouse.moveClick(upLocation)
                self.mouse.findLocation(condense, region = navRegion.region)
            self.mouse.moveClick(self.mouse.location)
class Mouse:
    keys = Keys()
    def pressMouse(self):
        self.keys.directMouse(buttons=self.keys.mouse_lb_press)
        sleep(0.1)
        self.keys.directMouse(buttons=self.keys.mouse_lb_release)
        sleep(1)
    def clickCenter(self,imgName, con = 0.98, region = (0,0,pyautogui.size().width,pyautogui.size().height)):
        self.moveMouse(imgName, region = region)
        self.pressMouse()
    def moveMouse(self,imgName, con = 0.98, region = (0,0,pyautogui.size().width,pyautogui.size().height)):
        location = pyautogui.locateCenterOnScreen(imgName, confidence = con, region = region)
        pyautogui.moveTo(location)
    def findLocation(self,imgName, con = 0.98, region = (0,0,pyautogui.size().width,pyautogui.size().height)):
        location = pyautogui.locateCenterOnScreen(imgName, confidence = con, region = region)
        self.location = location
    def moveClick(self, location):
        pyautogui.moveTo(location)
        self.pressMouse()





class Region:
    def __init__(self, region = (None,None,None,None)):
        self.region = region
        self.left = region[0]
        self.top = region[1]
        self.width = region[2]
        self.height = region[3]
    def gameRegion(self):
        gameHandle = FindWindow(None, "Dungeon Fighter Online")
        gameWindow = GetWindowRect(gameHandle)
        self.region = (gameWindow[0], gameWindow[1], gameWindow[2]-gameWindow[0], gameWindow[3]-gameWindow[1])
        self.left = self.region[0]
        self.top = self.region[1]
        self.width = self.region[2]
        self.height = self.region[3]
    def findsubRegion(self, region, con = 0.98):
        location = pyautogui.locateOnScreen(region,confidence = con, region=self.region)
        self.verticalSpacing = location.height
        self.topSub = location.top
