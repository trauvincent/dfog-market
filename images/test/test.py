

import os
import re
import cv2
def readData():
    list = []
    files = os.listdir("images/test")
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join("images/test", file)) as f:
                text = f.read()
                list.append((text, file))
    print(*list,  sep="\n")
    return list
"""
def createGroundTruth():
    number = 0

    while number < 612:
        with open(f"item{number}.gt.txt", "w+") as f:   # Opens file and casts as f
            f.write(pytesseract.image_to_string(f"item{number}.png", config = '--psm 6'))
        with open(f"cost{number}.gt.txt", "w+") as f:
            f.write(pytesseract.image_to_string(f"cost{number}.png", config = '--psm 6'))
        number += 1
"""
def removeImages():
    files = os.listdir(".")
    for file in files:
        if file.startswith('item') and file.endswith(".png"):
            print(file)
            img = cv2.imread(file)
            if img.shape[0] > 50:
                os.remove(file)
                file = file.replace(".png",".gt.txt")
                os.remove(file)
def removeWhite():
    files = os.listdir(".")
    for file in files:
        if file.startswith('item') and file.endswith(".png"):
            print(file)
            img = cv2.imread(file)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            coords = cv2.findNonZero(gray)
            x, y, w, h = cv2.boundingRect(coords)
            rect = img[y-7:y+h+7, x-7:x+w+7]
            cv2.imwrite(file, rect)

def divideData():
    number = 4899
    cost = 4899
    item = 4899
    l = []
    files = os.listdir("images/test")
    for file in files:
        string = ""
        text_file = open(f'images/test/{number}.gt.txt','r')
        line_list = text_file.readlines()
        for line in line_list:
            string += line
        text_file.close()
        if "Total" in string:
            os.rename(f'images/test/{number}.gt.txt',f'images/test/cost{cost}.gt.txt')
            os.rename(f'images/test/{number}.png',f'images/test/cost{cost}.png')
            cost += 1
        else:
            os.rename(f'images/test/{number}.gt.txt',f'images/test/item{item}.gt.txt')
            os.rename(f'images/test/{number}.png',f'images/test/item{item}.png')
            item += 1
        number += 1



def readData():
    list = []
    files = os.listdir("images/test")
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join("images/test", file)) as f:
                text = f.read()
                list.append(text)
    print(*list,  sep="\n")
    return list



def main():
    removeImages()



if __name__ == '__main__':

    main()
