import cv2
import time
from threading import Thread

class CaptureThread(Thread):
    """Thread class for video capture"""

    def __init__(self, q):
        Thread.__init__(self)
        self.video_source = cv2.VideoCapture(0)
        self.q = q
        self.active = True

    def run(self):
        print(" > Starting Video Capture Thread")
        while self.active:
            res, frame = self.video_source.read()
            self.q.put(frame)
            time.sleep(0.01)

    def deactivate(self):
        print(" > Stoping Video Capture Thread")
        self.active = False

