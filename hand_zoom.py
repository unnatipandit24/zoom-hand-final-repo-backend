import cv2
import mediapipe as mp
import math

class HandZoomDetector:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils
        self.zoom = 1.0

    def process_frame(self, frame):
        # Convert to RGB for Mediapipe
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Thumb tip (4), Index tip (8)
                x1, y1 = hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y
                x2, y2 = hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y

                h, w, _ = frame.shape
                x1, y1, x2, y2 = int(x1 * w), int(y1 * h), int(x2 * w), int(y2 * h)

                distance = math.hypot(x2 - x1, y2 - y1)
                self.zoom = max(1.0, min(distance / 50, 3.0))  # Clamp zoom between 1–3x

                self.mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

        return self.zoom
