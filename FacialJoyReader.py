from SoundControl import SoundControl
from WebCamCapture import WebCamCapture
from PictureAnalysis import PictureAnalysis, Context, Facial
import time



class FacialJoyReader:
    face_joy=Facial()

    def find_joy_levels(self, file_name):
        analysis = PictureAnalysis()
        face_joy = analysis.analyse_picture(file_name, Context.FACIAL)

new_item = FacialJoyReader()
new_item.find_joy_levels("capture/funeral2.jpg")
new_item.find_joy_levels("capture/awesome.jpg")