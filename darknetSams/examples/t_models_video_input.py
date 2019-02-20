import argparse
import sys

import cv2
import os
import time
# Root directory of the project
# ROOT_DIR = os.path.abspath("../")
# os.chdir(ROOT_DIR)

from darknetSams.models import Logo, Coco, Cart


def t_video(args):
    video_path = os.path.expanduser(os.path.join("~/Downloads", "stock_market.mp4"))
    cap = cv2.VideoCapture(video_path)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 1200, 1000)
    if args['model'] == 'coco':
        cv_model = Coco()
    elif args['model'] == 'logo':
        cv_model = Logo()
    else:
        return -1

    while cap.isOpened():
        ret, frame = cap.read()

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if ret:
            t1 = time.time()
            masked_frame, r = cv_model.detect_frame(frame, verbose=0, draw_results=True)
            t2 = time.time()
            print("FPS: {:.2f}".format(1/(t2-t1)))
            cv2.imshow('frame', masked_frame)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--model", type=str, default='coco',
                    help="Choose the model")
    args = vars(ap.parse_args())
    t_video(args)



