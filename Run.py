import cv2
import numpy as np
import smtplib
import playsound
import threading
import time

# Global status flags
Alarm_Status = False
Email_Status = False
Fire_Reported = 0
fire_frame_count = 0  # Counts how many continuous frames fire is seen


# --- Play Alarm Sound ---
def play_alarm_sound_function():
    for i in range(5):  # Play alarm 8 times
        print(f"🔊 Playing alarm sound ({i+1}/5)")
        playsound.playsound('Fire Alarm Sound.mp3', True)
        time.sleep(0.5)
    print(" Alarm sound finished playing.")


# --- Send Email Alert ---
def send_mail_function():
    recipientEmail = "abishekpandian2003@gmail.com"
    recipientEmail = recipientEmail.lower()

    try:
        subject = " Fire Alert!"
        body = (
            "Warning: A fire accident has been detected at our Chemical Plant.\n"
            "Please take immediate action to ensure safety."
        )
        message = f"Subject: {subject}\n\n{body}"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("21bit101@americancollege.edu.in", "uhmy kiqa fzqz euaz")
        server.sendmail("21bit101@americancollege.edu.in", recipientEmail, message.encode('utf-8'))
        print(f" Email sent successfully to {recipientEmail}")
        server.close()

    except Exception as e:
        print(" Email sending failed:", e)


# --- Choose Input Source ---
print("Select video source:")
print("1️⃣  Webcam (live)")
print("2️⃣  Video file (enter filename)")
choice = input("Enter your choice (1 or 2): ").strip()

if choice == "1":
    print("Starting webcam...")
    video = cv2.VideoCapture(0)
else:
    video = cv2.VideoCapture("Fire video 1.mp4")

if not video.isOpened():
    print(" Error: Could not open video source.")
    exit()

# --- Fire Detection Loop ---
while True:
    grabbed, frame = video.read()
    if not grabbed:
        print(" Video stream ended or failed.")
        break

    frame = cv2.resize(frame, (960, 540))
    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # --- Improved Fire color range ---
    lower_fire1 = np.array([0, 150, 150])
    upper_fire1 = np.array([35, 255, 255])
    mask1 = cv2.inRange(hsv, lower_fire1, upper_fire1)

    # Optional: detect higher red hue range
    lower_fire2 = np.array([160, 150, 150])
    upper_fire2 = np.array([179, 255, 255])
    mask2 = cv2.inRange(hsv, lower_fire2, upper_fire2)

    mask = cv2.add(mask1, mask2)

    # --- Morphological filtering to remove small noise ---
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    fire_detected = False
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 3000:  # Only count big enough areas
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, " Fire Detected!", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            fire_detected = True

    # --- Stabilization: trigger only if fire persists for few frames ---
    if fire_detected:
        fire_frame_count += 1
    else:
        fire_frame_count = 0

    if fire_frame_count > 3:  # Fire visible for 3 consecutive frames
        Fire_Reported += 1

        if not Alarm_Status:
            threading.Thread(target=play_alarm_sound_function).start()
            Alarm_Status = True

        if not Email_Status:
            threading.Thread(target=send_mail_function).start()
            Email_Status = True

    cv2.imshow(" Fire Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(" Exiting program...")
        break

cv2.destroyAllWindows()
video.release()
