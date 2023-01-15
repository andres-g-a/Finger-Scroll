import cv2
import time
import argparse
import pyautogui

from models import HandDetector


def main():

    video_capture = cv2.VideoCapture(0)
    hand_detector = HandDetector(min_detection=0.5)

    while True:

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Detect hands
        hand_detector.find_hands(frame)

        # Get up fingers
        up_fingers = hand_detector.get_up_fingers(frame)

        if up_fingers:

            if up_fingers[1]:
                # scroll up
                pyautogui.scroll(2)

            if not up_fingers[1]:
                # scroll down
                pyautogui.scroll(-2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            break

    # When everything is done, release the capture
    video_capture.release()


if __name__ == '__main__':
    main()
