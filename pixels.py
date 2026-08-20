import cv2
import numpy as np

# Create a 400 x 400 black image
image = np.zeros((400, 400), dtype=np.uint8)

# Create a white square in the center
image[100:300, 100:300] = 255

# Display the image
cv2.imshow("Black and White Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()