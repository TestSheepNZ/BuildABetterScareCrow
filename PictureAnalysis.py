from SoundControl import SoundControl
from WebCamCapture import WebCamCapture
from GoogleVisionRequest import GoogleVisionRequest
import time
from enum import Enum

class Context(Enum):
    LABEL = 1
    FACIAL = 2

LIKELIHOOD_TYPES = [
    'UNKNOWN',
    'VERY_UNLIKELY',
    'UNLIKELY',
    'POSSIBLE',
    'LIKELY',
    'VERY_LIKELY',
]


def get_likelihood_num(like_type):
    """Return the Vision API symbol corresponding to the given number."""
    for i in range (0, len(LIKELIHOOD_TYPES)):
        if (like_type == LIKELIHOOD_TYPES[i]):
            return i
    else:
        return 0

def get_likelihood_type(like_num):
    """Return the Vision API symbol corresponding to the given number."""
    like_num = int(like_num)
    if 0 < like_num < len(LIKELIHOOD_TYPES):
        return LIKELIHOOD_TYPES[like_num]
    else:
        return LIKELIHOOD_TYPES[0]

class Label:
    description = ""
    score = 0

class Facial:
    number_people = 0
    joy = 0
    sorrow = 0
    anger = 0
    surprise = 0
    underexposed = 0
    blurred = 0
    headwear = 0
    confidence = 0

    def add(self, other):
        self.number_people = self.number_people + other.number_people
        self.joy = self.joy + other.joy
        self.sorrow = self.sorrow + other.sorrow
        self.anger = self.anger + other.anger
        self.surprise = self.surprise + other.surprise
        self.underexposed = self.underexposed + other.underexposed
        self.blurred = self.blurred + other.blurred
        self.headwear = self.headwear + other.headwear

    def get_average_joy(self):
        return self.joy / self.number_people

    def get_average_sorrow(self):
        return self.sorrow / self.number_people

    def get_average_anger(self):
        return self.anger / self.number_people

    def get_average_surprise(self):
        return self.surprise / self.number_people

    def get_average_underexposed(self):
        return self.underexposed / self.number_people

    def get_average_blurred(self):
        return self.blurred / self.number_people

    def get_average_headwear(self):
        return self.headwear / self.number_people

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

    def matches_label(self, label_name, label_score, current_priority):
        current_time = time.time()
        if current_time > self.cooldown:
            for this_tag in self.tag_list:
                if this_tag in label_name:
                    if label_score > self.threshold:
                        if self.priority < current_priority:
                            return True
        return False

    def get_priority(self):
        return self.priority

    def trigger_response(self):
        self.set_triggered()
        sound_display = SoundControl()
        sound_display.sound_and_picture_display(self.audio_response, self.visual_response, "API Matched Item")


class PictureAnalysis:
    vision_api_matches_list = list()
    items_of_interest_list = list()
    google_request = GoogleVisionRequest()
    snap_shot = 0
    request_mode = Context.LABEL
    features = "4:20"
    confidence_threshold = 0.75

    #sets the type of request asked for - currently label analysis or facial read
    def __set_context__(self, request):
        if request == Context.FACIAL:
            self.request_mode = Context.FACIAL
            self.features = "1:20"
        else:
            self.request_mode = Context.LABEL
            self.features = "4:20"

    def take_picture(self, request):
        if self.snap_shot == 0:
            self.snap_shot = WebCamCapture()
        features = "4:20"

        if (self.snap_shot.picture_countdown()):
            self.analyse_picture(self.snap_shot.get_picture_name(), request)

    def analyse_picture(self, picture_file, request):
        self.vision_api_matches_list.clear()
        self.__set_context__(request)

        if (self.google_request.prepare_picture(picture_file, self.features)):
            if (self.google_request.send_picture_to_api()):
                try:
                    datalist = self.google_request.get_json_datalist()

                    if self.request_mode == Context.FACIAL:
                        self.__facial_analaysis__(datalist)
                    else:
                        self.__label_analysis__(datalist)

                except:
                    sound_display = SoundControl()
                    sound_display.error_blip()
                    print("Issue with Google Vision API data")

    def __label_analysis__(self, datalist):
        try:
            for responseItem in datalist['responses']:
                for label_item in responseItem['labelAnnotations']:
                    label_details = Label()
                    label_details.description = label_item['description']
                    label_details.score = label_item['score']
                    self.vision_api_matches_list.append(label_details)

            print("API Response")
            for this_thing in self.vision_api_matches_list:
                print(this_thing.description + " = " + str(this_thing.score))

            picture_match = False
            current_match = ItemOfInterest()
            current_match.priority = 100

            for visual_label in self.vision_api_matches_list:
                for item_of_interest in self.items_of_interest_list:
                    if item_of_interest.matches_label(visual_label.description, visual_label.score,
                                                      current_match.priority):
                        current_match = item_of_interest
                        picture_match = True

            if picture_match:
                current_match.trigger_response()
            else:
                print("No match")
                # snap_shot.deletePicture()
        except:
            sound_display = SoundControl()
            sound_display.error_blip()
            print("Issue processing data returned from Google Vision API")

    def __facial_analaysis__(self, datalist):
        try:
            total_face_data = Facial()

            for responseItem in datalist['responses']:
                for face_item in responseItem['faceAnnotations']:
                    confidence = face_item['detectionConfidence']
                    if (confidence >= self.confidence_threshold):
                        this_face = Facial()
                        this_face.joy = get_likelihood_num(face_item['joyLikelihood'])
                        this_face.sorrow = get_likelihood_num(face_item['sorrowLikelihood'])
                        this_face.surprise = get_likelihood_num(face_item['surpriseLikelihood'])
                        this_face.underexposed = get_likelihood_num(face_item['underExposedLikelihood'])
                        this_face.blurred = get_likelihood_num(face_item['blurredLikelihood'])
                        this_face.headwear = get_likelihood_num(face_item['headwearLikelihood'])
                        this_face.number_people = 1

                        total_face_data.add(this_face)

            print()
            print("People with confident facial readings " + str(total_face_data.number_people))
            print("Average joy " + str(total_face_data.get_average_joy()))
            print(get_likelihood_type(int(0.5 + total_face_data.get_average_joy())))

            return total_face_data

        except:
            print("Issues with response for facial data")
