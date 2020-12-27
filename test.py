import unittest
from classes import *

class TestTesseract(unittest.TestCase):
    def test_image(self):
        count = 0
        itemData = Data("cost")
        dictionary = itemData.dictionary
        for image in dictionary:
            img = cv2.imread(image)
            #img = cv2.bitwise_not(img)
            #img = cv2.blur(img, (4,4))
            img = cv2.GaussianBlur(img,(7,7),0)
            #kernel = np.ones((2,2), np.uint8)
            #img = cv2.dilate(img, kernel, iterations=1)
            #img = cv2.erode(img, kernel, iterations = 1)
            #cv2.imshow("image", img)
            #cv2.waitKey(0)
            #whitelist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890(&!+,):-+[%]./\\'\\ "
            whitelist = "1234567890,"
            custom_config = f"-c tessedit_char_whitelist={whitelist} --psm 6 -l engBest"
            ocr = pytesseract.image_to_string(img, config = custom_config)
            ocr = ocr.strip()

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