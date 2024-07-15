import cv2

# Open the camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("Error: Could not open camera.");
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    # Convert the frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Define the size of the square
    square_size = 50

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]
    sat_value = pixel_center[1]
    val_value = pixel_center[2]

    color = "Undefined"
    if val_value < 50:
        color = "BLACK"
    elif val_value > 200 and sat_value < 40:
        color = "WHITE"
    elif hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    elif hue_value >= 10 and hue_value <= 20 and sat_value > 100 and val_value > 20 and val_value < 200:
        color = "BROWN"
    elif hue_value >= 160 and hue_value <= 170 and sat_value > 100 and val_value > 200:
        color = "PINK"
    else:
        color = "RED"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.rectangle(frame, (cx - square_size // 2, cy - square_size // 2),
                  (cx + square_size // 2, cy + square_size // 2), (0, 255, 0), 3)  # Neon green color

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:  # Exit on ESC key
        break

cap.release()
cv2.destroyAllWindows()
