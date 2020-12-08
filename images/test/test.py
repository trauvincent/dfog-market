
import pytesseract
import os
import re
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
def createGroundTruth():
    number = 0

    while number < 612:
        with open(f"item{number}.gt.txt", "w+") as f:   # Opens file and casts as f
            f.write(pytesseract.image_to_string(f"item{number}.png", config = '--psm 6'))
        with open(f"cost{number}.gt.txt", "w+") as f:
            f.write(pytesseract.image_to_string(f"cost{number}.png", config = '--psm 6'))
        number += 1

def divideData():
    number = 0
    cost = 0
    item = 0
    l = []
    files = os.listdir("images/test")
    for file in files:
        string = ""
        text_file = open(f'{number}.gt.txt','r')
        line_list = text_file.readlines()
        for line in line_list:
            string += line
        text_file.close()
        if "Total" in string:
            os.rename(f'{number}.gt.txt',f'cost{cost}.gt.txt')
            os.rename(f'{number}.png',f'cost{cost}.png')
            cost += 1
        else:
            os.rename(f'{number}.gt.txt',f'item{item}.gt.txt')
            os.rename(f'{number}.png',f'item{item}.png')
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
    print(*list,  sep="\n)
    return list



def main():
    divideData()



if __name__ == '__main__':

    main()
