import cv2
# cv2 baray pardazesh tasvir va labeeha

image_path = 'c:\\MY FILES\\pictures\\Screenshot_20221014-185651.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image at {image_path}")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
    edges = cv2.Canny(blurred_image, 15, 35)

    cv2.imshow('Original Image', image)
    cv2.imshow('Edges', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
