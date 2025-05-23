import cv2 as cv 

img_path = "Part-2/dog.jpg"
img = cv.imread(img_path)

red_channel = img.copy()
green_channel = img.copy()
blue_channel = img.copy()

print(img.shape) # (187, 269, 3)

width = img.shape[1]
height = img.shape[0]

for y in range(height):
    for x in range(width):
        red_channel[y, x, 1] = 0
        red_channel[y, x, 0] = 0
        
        green_channel[y, x, 2] = 0
        green_channel[y, x, 0] = 0
        
        blue_channel[y, x, 2] = 0
        blue_channel[y, x, 1] = 0

cv.imshow("red channel", red_channel)
cv.imshow("green channel", green_channel)
cv.imshow("blue channel", blue_channel)
cv.waitKey(0)
