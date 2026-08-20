import cv2
import numpy as np

height = 400
width = 700

# HSV image
hsv = np.zeros((height, width, 3), dtype=np.uint8)

# Hue changes from left to right
for x in range(width):
    hsv[:, x] = (int(x * 180 / width), 255, 255)

# Convert HSV to BGR
rainbow = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("Rainbow Gradient", rainbow)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()