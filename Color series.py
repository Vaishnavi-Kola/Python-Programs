import cv2
import numpy as np

# Create a blank image
height = 600
width = 400

img = np.zeros((height, width, 3), dtype=np.uint8)

# Height of each strip
strip_height = 100

# Colors (BGR format)
colors = [
    (0, 0, 0),          # Black
    (64, 64, 64),       # Dark Grey
    (128, 128, 128),    # Grey
    (192, 192, 192),    # Light Grey
    (255, 255, 255),    # White
    (128, 128, 128)     # Grey
]

# Draw horizontal strips
for i, color in enumerate(colors):
    start = i * strip_height
    end = start + strip_height
    img[start:end, :] = color

# Display the image
cv2.imshow("Horizontal Black-White-Grey Strips", img)

cv2.waitKey(0)
cv2.destroyAllWindows()