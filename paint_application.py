# Import libraries
import numpy as np
import cv2

# Initialize the canvas
canvas = np.ones([500, 1000, 3], 'uint8')

# Global variables
radius = 2
color = (0, 255, 0)  # Setting the color to green
pressed = False


# click callback
# Start drawing when the mouse is clicked once and stop on when the mouse is double clicked
def click(event, x, y, flags, param):
    global canvas, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas, (x, y), radius, color, -1)
    elif event == cv2.EVENT_MOUSEMOVE and pressed:
        cv2.circle(canvas, (x, y), radius, color, -1)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        pressed = False


# Initialize window and callback assignment
win_name = "Let's Paint"
cv2.namedWindow(win_name)
cv2.setMouseCallback(win_name, click)

while True:
    # Display the canvas
    cv2.imshow(win_name, canvas)

    # Add text to canvas
    txt = "Press g for green, b for blue, r for red and y for yellow. Press ecs to finish."
    cv2.putText(canvas, txt, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255))

    # key capture
    ch = cv2.waitKey(1)
    if ch & 0xFF == 27:
        cv2.imwrite("file.png", canvas)
        break
    elif ch & 0xFF == ord('b'):
        color = (255, 0, 0)
    elif ch & 0xFF == ord('r'):
        color = (0, 0, 255)
    elif ch & 0xFF == ord('g'):
        color = (0, 255, 0)
    elif ch & 0xFF == ord('y'):
        color = (0, 255, 255)
