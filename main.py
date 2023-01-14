import cv2
import time
import argparse

from models import HandDetector


def main():

    video_capture = cv2.VideoCapture(0)
    hand_detector = HandDetector()

    while True:

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Detect hands
        frame = hand_detector.find_hands(frame)

        # Read coords
        coords_list = hand_detector.find_position(frame)
        # TODO : plot trace of the finger.
        cv2.circle(frame, (30, 10), radius=0, color=(0, 0, 255), thickness=-1)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            cv2.destroyAllWindows()
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':

    # parser = argparse.ArgumentParser(description='Hand Detector')
    # parser.add_argument('-f', '--foo', help='Description for foo argument', required=True)
    # parser.add_argument('-b', '--bar', help='Description for bar argument', required=True)
    # args = vars(parser.parse_args())

    main()
