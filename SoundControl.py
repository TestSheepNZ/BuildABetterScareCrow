from cv2 import *
from playsound import playsound
import numpy


class SoundControl:

    # Plays an error blip if something goes wrong
    def error_blip(self):
        try:
            playsound("sounds/error.wav")
        except:
            print("ERROR - File not found")

    def sound_and_picture_display (self, sound_file, image_file, window_label):
        try:
            img = cv2.imread(image_file)

            self.sound_and_image_display(sound_file,img,window_label)
        except:
            print("ERROR - File not found")
            self.error_blip()

    # Here raw image is passed
    def sound_and_image_display (self, sound_file, img, window_label):
        try:
            cv2.namedWindow(window_label, WINDOW_AUTOSIZE)
            cv2.imshow(window_label, img)
            if(sound_file != ""):
                playsound(sound_file)
            cv2.waitKey()
            cv2.destroyWindow(window_label)
        except:
            print("ERROR - File not found")
            self.error_blip()


    def justSound (self, soundFile):
        try:
            playsound(soundFile)
        except:
            print("ERROR - File not found")
            self.error_blip()




"""
item = SoundControl()
item.errorBlip()
item.soundAndImageDisplay("sounds/tone.wav", "images/apple.jpg")
item.justSound("sounds/tone.wav")
"""