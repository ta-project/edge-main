
import numpy as np
import cv2
from threading import Thread

class PrivateCarThread(Thread):
    """Thread class for private car recognition"""

    def __init__(self, q):
        Thread.__init__(self)
        self.font = self.cv2.FONT_HERSHEY_SIMPLEX
        self.car_cascade = self.cv2.CascadeClassifier('PrivateCarCascade.xml')
        self.q = q
        self.active = True

    def run(self):
        print(" > Starting private car recognition")

        while self.active:
            if not work_queue.empty():
                img = self.q.get()
                
            gray = self.cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            car = self.car_cascade.detectMultiScale(gray, 1.7,5,0,(200,200))  

          for (x,y,w,h) in car:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,'Private Car',(x-int(w/16),y-int(h/16)), font, 1.0, (51,51,255), 2, cv2.LINE_AA)
            cv2.imshow('imgcar',img)
            cv2.waitKey(1)

    def deactivate(self):
        print(" > Stoping Video Capture Thread")
        self.active = False