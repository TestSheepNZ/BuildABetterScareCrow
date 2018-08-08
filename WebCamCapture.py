from cv2 import *
import time
import os
from SoundControl import SoundControl

class WebCamCapture:
    picture_name = ""
    last_picture_taken = 0
    time_between_shots = 1
    display_captured_pic = True

    def __set_picture_name__(self):
        self.last_picture_taken = int(time.time())
        self.picture_name = "capture\picture_" + str(self.last_picture_taken) + ".jpg"

    def get_picture_name(self):
        return self.picture_name

    def set_displayed_captured_pic(self, value):
        self.display_captured_pic = value

    def picture_countdown(self):
        sound_display = SoundControl()
        short_pip = "sounds/short_tone.wav"
        long_pip = "sounds/short_tone.wav"
        sound_display.justSound(short_pip)
        time.sleep(0.5)
        sound_display.justSound(short_pip)
        time.sleep(0.5)
        sound_display.justSound(short_pip)
        time.sleep(0.5)
        sound_display.justSound(long_pip)
        return_val = self.take_picture()
        return return_val

    def take_picture(self):
        # initialize the camera
        try:
            sound_display = SoundControl()

            cam = VideoCapture(1)  # 1 -> index of camera
            if cam is None or not cam.isOpened():
                cam.release()
                cam = VideoCapture(0)

            s, img = cam.read()
            cam.release()
            sound_display.justSound("sounds/camera.wav")
            self.__set_picture_name__()
            if s:  # frame captured without any errors
                imwrite(self.picture_name, img)  # save image

                if self.display_captured_pic:
                    sound_display.sound_and_image_display("", img, "Captured Picture")

            else:
                sound_display.error_blip()
                return False
            return True

        except:
            print("No camera opened")
            return False

    def delete_picture(self):
        os.remove(self.picture_name)



