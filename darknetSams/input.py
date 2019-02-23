import argparse

import cv2
import os
import time
import sys

# Root directory of the project
# ROOT_DIR = os.path.abspath("../")
# os.chdir(ROOT_DIR)
from darknetSams.models import Logo, Coco, Cart


def camera(model="coco", camera_id=0):
    count = 0
    if model.lower() == 'cart':
        m = Cart()
    elif model.lower() == 'logo':
        m = Logo()
    else:
        m = Coco()

    WINDOW_NAME = "Camera :: {}".format(model)
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW_NAME, 1920, 1080)
    cap = cv2.VideoCapture(camera_id)
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            t1 = time.time()
            masked_frame, r = m.detect_frame(frame, verbose=False, draw_results=True)
            cv2.imshow(WINDOW_NAME, masked_frame)
            t2 = time.time()
            print("FPS: {:.2f}".format(1 / (t2 - t1)))
            count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def video(video_path, model="coco"):
    video_path = os.path.expanduser(video_path)
    assert os.path.isfile(video_path) is True
    # video_path = os.path.expanduser(os.path.join("~/Documents", "videos", "20190217", "94", "20190217-103033-0.avi"))

    cap = cv2.VideoCapture(video_path)
    WINDOW_NAME = "Video :: {}".format(model)
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW_NAME, 1920, 1080)
    if model.lower() == 'cart':
        m = Cart()
    elif model.lower() == 'logo':
        m = Logo()
    else:
        m = Coco()

    while cap.isOpened():
        ret, frame = cap.read()

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if ret:
            t1 = time.time()
            masked_frame, r = m.detect_frame(frame, verbose=0, draw_results=True)
            t2 = time.time()
            print("FPS: {:.2f}".format(1 / (t2 - t1)))
            cv2.imshow(WINDOW_NAME, masked_frame)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
