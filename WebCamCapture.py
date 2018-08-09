from cv2 import *
import time
import os
from SoundControl import SoundControl


class WebCamCapture:
    picture_name = ""
    last_picture_taken = 0
    time_between_shots = 1
    display_captured_pic = True
    camera_countdown_on = True
    cam = 0

    def __set_picture_name__(self):
        self.last_picture_taken = int(time.time())
        self.picture_name = "capture\picture_" + str(self.last_picture_taken) + ".jpg"

    def get_picture_name(self):
        return self.picture_name

    def set_displayed_captured_pic(self, value):
        self.display_captured_pic = value

    def set_camera_countdown(self, value):
        self.camera_countdown_on = value

    def picture_countdown(self):
        sound_display = SoundControl()
        if(self.camera_countdown_on):
            short_pip = "sounds/short_tone.wav"
            long_pip = "sounds/short_tone.wav"
            sound_display.justSound(short_pip)
            time.sleep(0.5)
            sound_display.justSound(short_pip)
            time.sleep(0.5)
            sound_display.justSound(short_pip)
            time.sleep(0.5)
            sound_display.justSound(long_pip)
        return_val = self.__get_picture_from_camera__()
        return return_val

    def __init_camera__(self):
        self.camera_initialised = True
        self.cam = VideoCapture(1)  # 1 -> index of camera
        if self.cam  is None or not self.cam.isOpened():
            self.cam.release()
            self.cam = VideoCapture(0)

    def __get_picture_from_camera__(self):
        # initialize the camera
        try:
            sound_display = SoundControl()
            if (self.cam == 0):
                self.__init_camera__()

            s, img = self.cam.read()

            sound_display.justSound("sounds/camera.wav")
            self.__set_picture_name__()
            if s:  # frame captured without any errors
                imwrite(self.picture_name, img)  # save image

                if self.display_captured_pic:
                    sound_display.sound_and_image_display("", img, "Captured Picture")

            else:
                sound_display.error_blip()
                self.cam.release()
                return False

            #self.cam.release()
            #cv2.destroyAllWindows()

            return True

        except:
            print("No camera opened")
            return False

    def delete_picture(self):
        os.remove(self.picture_name)



