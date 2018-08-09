from SoundControl import SoundControl
from WebCamCapture import WebCamCapture
from PictureAnalysis import *
import time



class FacialJoyReader:
    face_joy = Facial()

    def find_joy_levels(self, file_name):
        analysis = PictureAnalysis()
        #new_face = Facial()
        new_face = analysis.analyse_picture(file_name, Context.FACIAL)
        self.face_joy.add(analysis.face_data)

    def overall_joy(self):
        print()
        print("OVERALL TOTAL")
        print("=============")
        print("People with confident facial readings " + str(self.face_joy.number_people))
        print("Average joy " + str(self.face_joy.get_average_joy()))
        print(get_likelihood_type(int(0.5 + self.face_joy.get_average_joy())))

new_item = FacialJoyReader()
new_item.find_joy_levels("capture/agiletd1.jpg")
new_item.find_joy_levels("capture/agiletd2.jpg")
new_item.find_joy_levels("capture/agiletd3.jpg")
new_item.find_joy_levels("capture/agiletd4.jpg")
new_item.find_joy_levels("capture/agiletd5.jpg")
new_item.find_joy_levels("capture/agiletd6.jpg")
new_item.find_joy_levels("capture/agiletd7.jpg")
new_item.find_joy_levels("capture/agiletd8.jpg")
new_item.find_joy_levels("capture/agiletd9.jpg")
new_item.find_joy_levels("capture/agiletd10.jpg")
new_item.find_joy_levels("capture/agiletd11.jpg")
new_item.find_joy_levels("capture/agiletd12.jpg")
new_item.overall_joy()