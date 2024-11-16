import cv2 as cv

img_path = "Part-2/dog.jpg"

img = cv.imread(img_path)
img2 = img.copy()
img3 = img.copy()

width = img.shape[1]
height = img.shape[0]

def adjust_color(color, number):
    new_color = color + number

    if new_color < 0:
        return 0
    elif new_color > 255:
        return 255
    else:
        return new_color

num1 = int(input("Enter a number? "))
num2 = int(input("Enter a number? "))

for i in range(height):
    for j in range(width):
        red_channel = img[i][j][2]
        green_channel = img[i][j][1]
        blue_channel = img[i][j][0]

        img2[i][j][2] = adjust_color(red_channel, num1)
        img2[i][j][1] = adjust_color(green_channel, num1)
        img2[i][j][0] = adjust_color(blue_channel, num1)

        img3[i][j][2] = adjust_color(red_channel, num2)
        img3[i][j][1] = adjust_color(green_channel, num2)
        img3[i][j][0] = adjust_color(blue_channel, num2)


cv.imshow("Original Image", img)
cv.imshow("Adjusted Image 1", img2)
cv.imshow("Adjusted Image 2", img3)
cv.waitKey(0)
cv.destroyAllWindows()