import cv2 as cv 

img_path = "Part-2/dog.jpg"

img = cv.imread(img_path)

x = int(input("x: "))
y = int(input("y: "))

print(img[y, x]) # [116 144 191] [B G R]

r = img[y, x][2]
g = img[y, x][1]
b = img[y, x][0]

print(f"red: {r}")
print(f"green: {g}")
print(f"blue: {b}")

img[y, x] = [0, 0, 255]

cv.imshow("image", img)
cv.waitKey(0)
