import unittest

class TestSum(unittest.TestCase):
"""
for b in emblem:
    print(b)
    string2 = f"images/{b}.png"

    location2 = pyautogui.locateOnScreen(string2,confidence = 0.98)

    location2 = pyautogui.center(location2)
    while location2 is None:
        pyautogui.moveTo(downLocation)
        pressMouse()
        sleep(1)
        pyautogui.moveTo(resetLocation)
        location2 = pyautogui.locateCenterOnScreen(string2,confidence = 0.98)
    pyautogui.moveTo(location2)
    pressMouse()
    sleep(1)

    for c in colorType[b]:
        print(c)
        string3 = f"images/{c}.png"
        location3 = pyautogui.locateCenterOnScreen(string3,confidence = 0.98)
        while location3 is None:
            pyautogui.moveTo(downLocation)

            sleep(1)
            pressMouse()
            pyautogui.moveTo(resetLocation)
            location3 = pyautogui.locateCenterOnScreen(string3,confidence = 0.98)
        pyautogui.moveTo(location3)
        pressMouse()
        sleep(1.5)


    sleep(1)
    pyautogui.moveTo(location2)
    pressMouse()
    sleep(1)

"""
