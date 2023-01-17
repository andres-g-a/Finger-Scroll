import numpy as np


def moves(theta, length=5):
    """Returns the lenght of move x and move y"""

    x = np.cos(np.radians(theta))*length
    y = np.sin(np.radians(theta))*length

    return int(x), int(y)


def get_angle(detection):
    """Returns the angle between two points in degrees between 0 and 360"""

    xp, yp = detection[5][1:]  # p
    xd, yd = detection[8][1:]  # d

    theta = -np.degrees(np.arctan2(yd-yp, xd-xp))

    return theta
