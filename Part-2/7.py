import math
import cv2 as cv
import numpy as np


img_path = "Part-2/dog.jpg"
img = cv.imread(img_path)

height = img.shape[0]
width = img.shape[1]

n = float(input("Enter a scaling number: "))

width2 = math.floor(width * n)
height2 = math.floor(height * n)

img2 = np.zeros((height2, width2, 3), np.uint8)

for y in range(height2-1):
    for x in range(width2-1):
        img2[y, x, 2] = img[math.ceil(y / n), math.ceil(x / n), 2]
        img2[y, x, 1] = img[math.ceil(y / n), math.ceil(x / n), 1]
        img2[y, x, 0] = img[math.ceil(y / n), math.ceil(x / n), 0]

cv.imshow("Original Image", img)
cv.imshow("Resized Image", img2)
cv.waitKey(0)
cv.destroyAllWindows()

