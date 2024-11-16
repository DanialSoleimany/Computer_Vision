import cv2 
import numpy as np

# مسیر تصویر ورودی
image_path = "Part-2\stones.jpg"
# خواندن تصویر به صورت رنگی
original_image = cv2.imread(image_path)
# کپی کردن تصویر برای اعمال تبدیل به خاکستری
gray_image = cv2.imread(image_path)
# ایجاد یک تصویر خالی برای ذخیره نتایج لبه‌یابی
edge_image = np.zeros_like(original_image)

original_image.shape
edge_image.shape

height = original_image.shape[0]
width = original_image.shape[1]

def convert_to_grayscale(input_image, height, width):
    """RGB تبدیل تصویر به مقیاس خاکستری با استفاده از مقادیر"""
    for y in range(height):
        for x in range(width):
            red = input_image[y, x, 2]
            green = input_image[y, x, 1]
            blue = input_image[y, x, 0]
            # محاسبه شدت خاکستری با استفاده از ترکیب وزنی
            grayscale_value = (red * 0.299) + (green * 0.587) + (blue * 0.144)
            gray_image[y, x] = [grayscale_value] * 3
            
    return gray_image

def get_neighborhood(data, y, x):
    """استخراج بلوک ۳×۳ از پیکسل‌های اطراف پیکسل مرکزی"""
    neighborhood = [
        [0, 0, 0], 
        [0, 0, 0], 
        [0, 0, 0]
    ]
    
    neighborhood[0][0] = data[y-1, x-1, 2]
    neighborhood[0][1] = data[y-1, x, 2]
    neighborhood[0][2] = data[y-1, x+1, 2]
    neighborhood[1][0] = data[y, x-1, 2]
    neighborhood[1][1] = data[y, x, 2]
    neighborhood[1][2] = data[y, x+1, 2]
    neighborhood[2][0] = data[y+1, x-1, 2]
    neighborhood[2][1] = data[y+1, x, 2]
    neighborhood[2][2] = data[y+1, x+1, 2]
    
    return neighborhood

def elementwise_multiply(matrix_a, matrix_b):
    """ضرب عنصر به عنصر دو ماتریس ۳×۳"""
    multiplied_matrix = []
    for i in range(len(matrix_a)):
        row_result = []
        for j in range(len(matrix_a)):
            row_result.append(matrix_a[i][j] * matrix_b[i][j])
        multiplied_matrix.append(row_result)
    return multiplied_matrix

def apply_filter(kernel, neighborhood):
    """اعمال ماسک ۳×۳ به بلوک پیکسل‌ها و محاسبه مجموع نتایج"""
    result = elementwise_multiply(kernel, neighborhood)
    total_sum = 0
    for i in range(3):
        for j in range(3):
            total_sum += result[i][j]
    return total_sum
# تبدیل تصویر به خاکستری
grayscale_data = convert_to_grayscale(original_image, height, width)

# تعریف ماسک‌های سوبل برای جهت‌های x و y
prewitt_x = [
    [-1, 1, 1],
    [-1, -2, 1], 
    [-1, 1, 1]
]

prewitt_y = [
    [1, 1, 1], 
    [-1, -2, 1], 
    [-1, -1, 1]
]

# محاسبه گرادیان تصویر با ماسک سوبل
for y in range(1, height - 1):
    for x in range(1, width - 1):
        neighborhood = get_neighborhood(grayscale_data, y, x)
        gradient_x = apply_filter(prewitt_x, neighborhood)
        gradient_y = apply_filter(prewitt_y, neighborhood)
        # ترکیب گرادیان‌های افقی و عمودی
        gradient_magnitude = gradient_x + gradient_y
        # محدود کردن مقادیر به بازه ۰ تا ۲۵۵
        gradient_magnitude = max(0, min(255, gradient_magnitude))
        edge_image[y, x] = [gradient_magnitude] * 3

# نمایش تصاویر
cv2.imshow("Original Image", original_image)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Edge Detected Image", edge_image)
cv2.waitKey(0)
cv2.destroyAllWindows()