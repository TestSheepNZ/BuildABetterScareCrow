from cv2 import *
from playsound import playsound
import numpy


class SoundControl:

    # Plays an error blip if something goes wrong
    def errorBlip(self):
        try:
            playsound("sounds/error.wav")
        except:
            print("ERROR - File not found")

    """
    def soundAndImageDisplay(self, soundFile, imageFile):
        self.soundAndImageDisplay(soundFile, imageFile, "image")
    """

    def soundAndImageDisplay (self, soundFile, imageFile, windowLabel):
        try:
            img = cv2.imread(imageFile)

            cv2.namedWindow(windowLabel, WINDOW_AUTOSIZE)
            cv2.imshow(windowLabel, img)
            playsound(soundFile)
            cv2.waitKey()
            cv2.destroyWindow(windowLabel)
        except:
            print("ERROR - File not found")
            self.errorBlip()

    def justSound (self, soundFile):
        try:
            playsound(soundFile)
        except:
            print("ERROR - File not found")
            self.errorBlip()


"""
item = SoundControl()
item.errorBlip()
item.soundAndImageDisplay("sounds/tone.wav", "images/apple.jpg")
item.justSound("sounds/tone.wav")
"""