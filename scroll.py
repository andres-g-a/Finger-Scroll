import cv2
import time
import argparse

import numpy as np
import pyautogui

from models import HandDetector

from utils import moves, get_angle


def main():

    video_capture = cv2.VideoCapture(0)
    hand_detector = HandDetector(min_detection=0.4)

    keys = {'up': False, 'down': False, 'left': False, 'right': False}

    while True:

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        frame = cv2.flip(frame, 1)

        # Detect hands
        hand_detector.find_hands(frame)

        # Get up fingers
        detection = hand_detector.find_position(frame)

        if detection:

            theta = get_angle(detection)

            speed_x, speed_y = moves(theta, length=10)

            if speed_x >= 0:
                if keys['left']:  # release left key
                    pyautogui.keyUp('left')
                    keys['left'] = False
                if not keys['right']:  # press right key
                    pyautogui.keyDown('right')
                    keys['right'] = True

            if speed_x < 0:
                if keys['right']:  # release right key
                    pyautogui.keyUp('right')
                    keys['right'] = False
                if not keys['left']:  # press left key
                    pyautogui.keyDown('left')
                    keys['left'] = True

            if speed_y >= 0:
                if keys['down']:  # release down key
                    pyautogui.keyUp('down')
                    keys['down'] = False
                if not keys['up']:  # press up key
                    pyautogui.keyDown('up')
                    keys['up'] = True

            if speed_y < 0:
                if keys['up']:  # release up key
                    pyautogui.keyUp('up')
                    keys['up'] = False
                if not keys['down']:  # press down key
                    pyautogui.keyDown('down')
                    keys['down'] = True

        else:
            # Release all keys
            if keys['up']:
                pyautogui.keyUp('up')
                keys['up'] = False
            if keys['down']:
                pyautogui.keyUp('down')
                keys['down'] = False
            if keys['left']:
                pyautogui.keyUp('left')
                keys['left'] = False
            if keys['right']:
                pyautogui.keyUp('right')
                keys['right'] = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            break

    # Release the capture
    video_capture.release()


if __name__ == '__main__':
    main()
