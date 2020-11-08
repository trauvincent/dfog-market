
import time
import cv2
import pyautogui









def main():


    itemlist = [weapon, armor, accessory, specialequip, weaponshape, recipe, consumable, avatar, cloneavatar, emblemavatar, cloneemblem, emblem, creature, profession, misc]
    joblist1 = [slayer, fighter, gunner, mage, priest, thief, lancer, agent]
    weaponlist1 = [shortsword, katana, bludgeon, zanbato, lightsabre]
    weaponlist2 = [knuckle, gauntlets, claw, boxinggloves, tonfa]
    weaponlist3 = [revolver, autogun, musket, handcannon, bowgun]
    weaponlist4 = [spear, pole, rod, staff, broomstick]
    weaponlist5 = [cross, rosary, totem, scythe, battleaxe]
    weaponlist6 = [dagger, dualblade, wand, chakra]
    weaponlist7 = [longlance, halberd, beamspear, javelin]
    weaponlist8 = [odachi, kodachi, squaresword, coreblade]
    armor = [cloth, leather, light, heavy, plate]
    partlist1 = [top, headshoulder, bottom, shoes, belt]
    accessory = [necklace, ring, bracelet, title]
    joblist2 = [maleslayer, femaleslayer, malefighter, femalefighter, malegunner, femalegunner, malemage,femalemage, malepriest, femalepriest, thief, knight, lancer,agent]
    specialequip = [subequip, magicstone, earrings]
    joblist3 = [maleslayer, femaleslayer, darkknight, malefighter, femalefighter, malegunner, femalegunner, malemage,femalemage,creator, malepriest, femalepriest, thief, knight, lancer,agent]
    recipe = [weapon, armor, accessory, specialequip]
    consumable = [package, consume, material, throwinstall, drawing, quest, misc]
    partlist2 = [hat, hair, face, top, bottom, shoes, torso, waist, skin]
    emblem = [red, yellow, green, blue, platinum, multi]
    multilist = [redgreen, yellowblue, threecolors]
    creature = [pet, redartifact, blueartifact, greenartifact]
    profession = [alchemist, animator, enchanter, material]
    

    """
   #coordinate of first item in auction hall
   itemX = 180
   itemY = 135

   #change in y to iterate to next item
   itemStepY = 38

   #find image in tabs
   #pyautogui.locateOnScreen('someButton.png', region=(40, 125, 90, 335))
   time.sleep(5)

   #find search button
   pyautogui.screenshot('my_screenshot.png')
   #pyautogui.locateOnScreen('someButton.png', region=(560, 75, 50, 35))
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



if __name__ == '__main__':

    main()
