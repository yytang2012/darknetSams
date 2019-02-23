import os

from darknetSams.input import video

if __name__ == '__main__':
    video_path = os.path.join("~/", "Videos", "2.mp4")
    video(video_path, model="coco")
