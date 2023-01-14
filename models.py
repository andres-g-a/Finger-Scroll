import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self, mode=False, max_hands=2, min_detection=0.5, model_complexity=1, min_track=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.min_detection = min_detection
        self.min_track = min_track
        self.model_complexity = model_complexity
        self.results = None

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.model_complexity,
                                         self.min_detection, self.min_track)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return img

    def find_position(self, img, hand_no=0, draw=True):

        landmark_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for index, lm in enumerate(my_hand.landmark):
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                landmark_list.append([index, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                # self.mp_draw.draw_landmarks(img, my_hand, self.mp_hands.HAND_CONNECTIONS)

        return landmark_list
