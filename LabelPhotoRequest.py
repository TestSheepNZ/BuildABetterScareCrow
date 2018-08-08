from SoundControl import SoundControl
from WebCamCapture import WebCamCapture
from GoogleVisionRequest import GoogleVisionRequest
import time

class Label:
    description = ""
    score=0

class ItemOfInterest:
    tag_list = list()
    threshold = 0
    priority = 0
    cooldown = 0
    last_triggered = 0
    next_trigger = 0
    audio_response = ""
    visual_response = ""

    def set_triggered(self):
        self.last_triggered = int(time.time())
        self.next_trigger = self.last_triggered + self.cooldown

    def matches_label(self, label_name, labelScore, current_priority):
        current_time = time.time()
        if current_time > self.cooldown:
            for this_tag in self.tag_list:
                if this_tag in label_name:
                    if labelScore > self.threshold:
                        if self.priority < current_priority:
                            return True
        return False

    def get_priority(self):
        return self.priority

    def trigger_response(self):
        self.set_triggered()
        sound_display = SoundControl()
        sound_display.soundAndImageDisplay(self.audio_response, self.visual_response, "API Matched Item")

class LabelPhotoRequest:

    label_list = list()
    item_list = list()
    google_request = GoogleVisionRequest()



    def take_picture(self):
        self.label_list.clear()
        snap_shot = WebCamCapture()
        features = "4:20"

        if (snap_shot.picture_countdown()):
            self.google_request.prepare_picture(snap_shot.get_picture_name(), features)
            if (self.google_request.send_picture_to_api()):
                try:
                    datalist = self.google_request.get_json_datalist()

                    for responseItem in datalist['responses']:
                        for label_item in responseItem['labelAnnotations']:
                            label_details = Label()
                            label_details.description = label_item['description']
                            label_details.score = label_item['score']
                            self.label_list.append(label_details)

                    print("API Response")
                    for this_thing in self.label_list:
                        print(this_thing.description + " = " + str(this_thing.score))

                    picture_match = False
                    current_match = ItemOfInterest()
                    current_match.priority = 100

                    for visual_label in self.label_list:
                        for item_of_interest in self.item_list:
                            if item_of_interest.matches_label(visual_label.description, visual_label.score, current_match.priority):
                                current_match = item_of_interest
                                picture_match = True

                    if picture_match:
                        current_match.trigger_response()
                    else:
                        print ("No match")
                        #snap_shot.deletePicture()
                except:
                    sound_display = SoundControl()
                    sound_display.error_blip()
                    print("Issue processing data returned from Google Vision API")




