import cv2
import pyautogui
import mediapipe as mp


class HandDetector:

    def __init__(self, mode=False, max_hands=2, min_detection=0.5, model_complexity=1, min_track=0.5):
        self.mode = mode
        self.results = None
        self.fingers_up = None
        self.min_track = min_track
        self.max_hands = max_hands
        self.min_detection = min_detection
        self.model_complexity = model_complexity

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.model_complexity,
                                         self.min_detection, self.min_track)

    def find_hands(self, img, draw=False):

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        return img

    def find_position(self, img, hand_no=0, draw=False):

        landmark_list = []
        if self.results.multi_hand_landmarks:

            my_hand = self.results.multi_hand_landmarks[hand_no]

            for index, lm in enumerate(my_hand.landmark):
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                landmark_list.append([index, cx, cy])

                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        return landmark_list

    def get_up_fingers(self, img):

        pos = self.find_position(img, draw=False)

        self.fingers_up = []
        if pos:
            # thumb
            self.fingers_up.append(pos[4][1] < pos[3][1] and (pos[5][0] - pos[4][0] > 10))
            # index
            self.fingers_up.append(pos[8][1] < pos[7][1] < pos[6][1])
            # middle
            self.fingers_up.append(pos[12][1] < pos[11][1] < pos[10][1])
            # ring
            self.fingers_up.append(pos[16][1] < pos[15][1] < pos[14][1])
            # pinky
            self.fingers_up.append(pos[20][1] < pos[19][1] < pos[18][1])

        return self.fingers_up

    def get_direction(self, img):

        pos = self.find_position(img, draw=False)

        return pos

        # if not pos:
        #     return None
        #
        # # index
        # index_x = pos[8][1]
        # index_y = pos[8][2]
        #
        # # wrist
        # wrist_x = pos[5][1]
        # wrist_y = pos[5][2]
        #
        # # return index_x, index_y, wrist_x, wrist_y
        # return pos[8]

