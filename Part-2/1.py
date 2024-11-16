import cv2 as cv 

img_path = "Part-2\dog.jpg"

img = cv.imread(img_path)

cv.imshow("image", img)
cv.waitKey(0)