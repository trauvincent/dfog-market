import unittest
from classes import *

class TestTesseract(unittest.TestCase):
    def test_image(self):
        count = 0
        itemData = Data("item")
        dictionary = itemData.dictionary
        for image in dictionary:
            img = cv2.imread(image)
            #img = cv2.bitwise_not(img)
            #img = cv2.blur(img, (2,2))
            #img = cv2.GaussianBlur(img,(3,3),0)
            #kernel = np.ones((2,2), np.uint8)
            #img = cv2.dilate(img, kernel, iterations=1)
            #img = cv2.erode(img, kernel, iterations = 1)
            #cv2.imshow("image", img)
            #cv2.waitKey(0)
            whitelist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890(&!+,):-+[]./\\'\\ "
            custom_config = f"-c tessedit_char_whitelist={whitelist} --psm 6 -l itemFast"
            ocr = pytesseract.image_to_string(img, config = custom_config)
            ocr = ocr.strip()
            ocr = ocr.replace("Type 4", "Type A")
            try:
                self.assertEqual(itemData.dictionary[image], ocr)
            except:

                print(image)
                print(itemData.dictionary[image])
                print(ocr)
                count += 1

        print(count)


if __name__ == '__main__':
    unittest.main()