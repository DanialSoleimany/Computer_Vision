import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_path = "Part-2/dog.jpg"
img = cv.imread(img_path)

b = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
r = img[:, :, 2].astype(float)

gray_img = (0.114 * b + 0.587 * g + 0.299 * r).astype(np.uint8)

cv.imshow("Original Image", img)
cv.imshow("Grayscale", gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
