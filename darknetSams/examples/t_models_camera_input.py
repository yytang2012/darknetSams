import argparse

import cv2
import os
import time
import sys

# Root directory of the project
# ROOT_DIR = os.path.abspath("../")
# os.chdir(ROOT_DIR)
from darknetSams.models import Logo, Coco, Cart


def t_models(args):
    cap = cv2.VideoCapture(0)
    count = 0
    if args['model'] == 'coco':
        cv_model = Coco()
    elif args['model'] == 'logo':
        cv_model = Logo()
    else:
        return -1

    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            t1 = time.time()
            masked_frame, r = cv_model.detect_frame(frame, verbose=False, draw_results=True)
            cv2.imshow("frame", masked_frame)
            t2 = time.time()
            print("FPS: {:.2f}, time: {}".format(1/(t2-t1), t2 - t1))
            count += 1

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
    t_models(args)




