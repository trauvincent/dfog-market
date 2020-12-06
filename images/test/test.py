
import pytesseract
import os

def createGroundTruth():
    number = 0

    while number < 127:
        with open(f"item{number}.gt.txt", "w+") as f:   # Opens file and casts as f
            f.write(pytesseract.image_to_string(f"item{number}.png", config = '--psm 6'))
        with open(f"cost{number}.gt.txt", "w+") as f:
            f.write(pytesseract.image_to_string(f"cost{number}.png", config = '--psm 6'))
        number += 1

def cleanData():
    number = 0
    l = []
    while number < 127:
        itemString = ""
        text_file = open(f"item{number}.gt.txt",'r')
        line_list = text_file.readlines()
        for line in line_list:
            itemString += line
        text_file.close()
        if itemString not in l:
            l.append(itemString)
        else:
            os.remove(f"item{number}.gt.txt")
            os.remove(f"item{number}.png")

        costString = ""
        text_file = open(f"cost{number}.gt.txt",'r')
        line_list = text_file.readlines()
        for line in line_list:
            costString += line

        text_file.close()
        if costString not in l:
            l.append(costString)
        else:
            os.remove(f"cost{number}.gt.txt")
            os.remove(f"cost{number}.png")
        number += 1




def main():
    cleanData()


if __name__ == '__main__':

    main()
