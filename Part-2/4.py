import cv2 as cv 

img_path = "Part-2/dog.jpg"
img = cv.imread(img_path)

img_to_gray = img.copy()

width = img.shape[1]
height = img.shape[0]

for i in range(height):
    for j in range(width):
        r = img[i, j, 2]
        g = img[i, j, 1]
        b = img[i, j, 0]

        gray = r * 0.299 + g * 0.587 + b * 0.144 
        img_to_gray[i, j, 2] = img_to_gray[i, j, 1] = img_to_gray[i, j, 0] = gray


cv.imshow("color image", img)
cv.imshow("gray image", img_to_gray)
cv.waitKey(0)