from threading import Thread
import time
import sys
import msvcrt
import os
import argparse
import queue
import cv2
from Feed.camera_feed import CaptureThread
from GUI.gui import GUI
from PrivateCar.private_recognition import PrivateCarThread


work_queue = queue.Queue(3)
camera_feed_thread = CaptureThread(work_queue)
private_car_thread = PrivateCarThread(work_queue)

def initialize():
    """ Initialziation and configuration """
    time.sleep(1)
    print(" > Camera feed initialization ... ")
    camera_feed_thread.start()
    private_car_thread.start()



def main():

    GUI.disclaimer()

    initialize()

    done = False
    while not done:

        #Live feed show
        if not work_queue.empty():
            frame = work_queue.get()
            cv2.imshow("Image", frame)
            cv2.waitKey(1)

        if msvcrt.kbhit():
            """Keyboard input handler only for Windows platform"""
            GUI.disclaimer()
            usr_in = msvcrt.getch()
            if usr_in == b'v':
                #  Start the private vehicle detection thread
                pass

            elif usr_in == b'c':
                #  Start the commercial vehicle detection thread
                pass

            elif usr_in == b'p':
                #  Start the pedestrian detection thread
                pass

            elif usr_in == b's':
                #  stop all detection threads
                pass

            elif usr_in == b'r':
                #  Stop all threads
                pass

            elif usr_in == b'h':
                os.system('cls')
                GUI.help()

            elif usr_in == b'q':
                camera_feed_thread.deactivate()
                camera_feed_thread.join()
                done = True


if __name__=="__main__":
    main()