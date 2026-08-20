import cv2
import numpy as np

# Create a white image
img = np.ones((500, 500, 3), dtype=np.uint8) * 255
temp = img.copy()

drawing = False
ix, iy = -1, -1

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, temp

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = img.copy()
            cv2.rectangle(temp, (ix, iy), (x, y), (255, 0, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)
        temp = img.copy()

# Create window and set mouse callback
cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", draw_rectangle)

while True:
    cv2.imshow("Draw Rectangle", temp)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()