import math
import cv2 as cv
import numpy as np

img_path1 = "Part-2/dog.jpg"
img_path2 = "Part-2/tree.png"

img1 = cv.imread(img_path1)
img2 = cv.imread(img_path2)

height = img1.shape[0]
width = img1.shape[1]

n = float(input("Enter a number? ")) # between 0 and 1
m = 1 - n
img3 = np.zeros((height, width, 3), np.uint8)

for y in range(height - 1):
    for x in range(width - 1):

        r1 = img1[y, x, 2]
        g1 = img1[y, x, 1]
        b1 = img1[y, x, 0]

        r2 = img2[y, x, 2]
        g2 = img2[y, x, 1]
        b2 = img2[y, x, 0]

        img3[y, x, 2] = math.floor((n * r1 + m * r2) / 2)
        img3[y, x, 1] = math.floor((n * g1 + m * g2) / 2)
        img3[y, x, 0] = math.floor((n * b1 + m * b2) / 2)


cv.imshow("Dog image", img1)
cv.imshow("Tree image", img2)
cv.imshow("Merged Image", img3)
cv.waitKey(0)
cv.destroyAllWindows()
