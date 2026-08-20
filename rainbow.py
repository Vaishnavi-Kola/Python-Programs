import cv2
import numpy as np

# Create a 700 x 500 black image
image = np.zeros((500, 700, 3), dtype=np.uint8)

# Rainbow colors in BGR format
colors = [
    (0, 0, 255),       # Red
    (0, 165, 255),     # Orange
    (0, 255, 255),     # Yellow
    (0, 255, 0),       # Green
    (255, 0, 0),       # Blue
    (130, 0, 75),      # Indigo
    (211, 0, 148)      # Violet
]

# Draw rainbow strips
height = 500 // 7

for i, color in enumerate(colors):
    y1 = i * height
    y2 = (i + 1) * height
    cv2.rectangle(image, (0, y1), (700, y2), color, -1)

# Display the rainbow
cv2.imshow("Rainbow Pattern", image)

cv2.waitKey(0)
cv2.destroyAllWindows()