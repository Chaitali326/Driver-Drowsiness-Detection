# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# mp_env\Scripts\activate
# python Driver_Drowsiness_Detection.py

import cv2
import mediapipe as mp
import numpy as np
import pygame
from threading import Thread

# Initialize sound
pygame.mixer.init()

def sound_alarm(path):
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)  # -1 makes it loop while drowsy
    except Exception as e:
        print(f"Error playing sound: {e}")

# Add a function to stop it
def stop_alarm():
    pygame.mixer.music.stop()


# EAR calculation (no scipy)
def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

def mouth_aspect_ratio(mouth):
    # Vertical distance between upper and lower lip
    A = np.linalg.norm(mouth[0] - mouth[1]) 
    # Horizontal distance between left and right corners
    B = np.linalg.norm(mouth[2] - mouth[3]) 
    mar = A / B
    return mar

# MediaPipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Webcam
cap = cv2.VideoCapture(0)

# Thresholds
EYE_THRESH = 0.20
COUNTER = 0
ALARM_ON = False

MOUTH_THRESH = 0.6  # Adjust this based on your camera distance
UPPER_LOWER_LIPS = [13, 14] # Points for top and bottom inner lip
LEFT_RIGHT_LIPS = [78, 308] # Points for left and right corners


# Eye landmark indices (MediaPipe)
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            mesh_points = np.array(
                [(int(p.x * w), int(p.y * h)) for p in face_landmarks.landmark]
            )

            # --- Inside the landmarks loop ---
            left_eye = mesh_points[LEFT_EYE]
            right_eye = mesh_points[RIGHT_EYE]
            # Get points for the mouth (Upper, Lower, Left, Right)
            mouth_pts = mesh_points[[13, 14, 78, 308]] 

            leftEAR = eye_aspect_ratio(left_eye)
            rightEAR = eye_aspect_ratio(right_eye)
            ear = (leftEAR + rightEAR) / 2.0
            
            mar = mouth_aspect_ratio(mouth_pts)

            # --- Logic for Drowsiness ---
            # Trigger if Eyes are closed OR Mouth is wide open (Yawn)
            if ear < EYE_THRESH or mar > MOUTH_THRESH:
                COUNTER += 1
                if COUNTER > 20:
                    status = "DROWSY!"
                    cv2.putText(frame, status, (20, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    if not ALARM_ON:
                        ALARM_ON = True
                        Thread(target=sound_alarm, args=("alert.wav",), daemon=True).start()
            else:
                COUNTER = 0
                if ALARM_ON:
                    ALARM_ON = False
                    pygame.mixer.music.stop()

            # Display stats on screen
            cv2.putText(frame, f"EAR: {ear:.2f} MAR: {mar:.2f}", (200, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()