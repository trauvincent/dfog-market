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
