from cv2 import *
import datetime
import time
import os
from SoundControl import SoundControl

class WebCamCapture:
    pictureName = ""
    lastPictureTaken = 0
    timeBetweenShots = 1
    displayCapturedPic = True

    def __setPictureName__(self):
        self.lastPictureTaken = int(time.time())
        self.pictureName = "capture\picture_" + str(self.lastPictureTaken) + ".jpg"

    def getPictureName(self):
        return self.pictureName

    def setDisplayedCapturedPic(self, value):
        self.displayCapturedPic = value


    def pictureCountdown(self):
        soundDisplay = SoundControl()
        shortPip = "sounds/short_tone.wav"
        longPip = "sounds/short_tone.wav"
        soundDisplay.justSound(shortPip)
        time.sleep(0.5)
        soundDisplay.justSound(shortPip)
        time.sleep(0.5)
        soundDisplay.justSound(shortPip)
        time.sleep(0.5)
        soundDisplay.justSound(longPip)
        returnVal = self.takePicture()
        return returnVal

    def takePicture(self):
        # initialize the camera
        try:
            soundDisplay = SoundControl()

            cam = VideoCapture(1)  # 1 -> index of camera
            if cam is None or not cam.isOpened():
                cam.release()
                cam = VideoCapture(0)

            s, img = cam.read()
            cam.release()
            soundDisplay.justSound("sounds/camera.wav")
            self.__setPictureName__()
            if s:  # frame captured without any errors
                imwrite(self.pictureName, img)  # save image

                if self.displayCapturedPic:
                    namedWindow("Captured Picture", WINDOW_AUTOSIZE)
                    imshow("Captured Picture", img)
                    waitKey(0)
                    destroyWindow("Captured Picture")
            else:
                soundDisplay.errorBlip()
                return False
            return True

        except:
            print("No camera opened")
            return False

    def deletePicture(self):
        os.remove(self.pictureName)

"""
picture = WebCamCapture()
picture.__setPictureName__()
if (picture.pictureCountdown()):
    picture.deletePicture()
"""
"""if (picture.takePicture()):
    picture.deletePicture()"""

