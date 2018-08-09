from SoundControl import SoundControl
from WebCamCapture import WebCamCapture
from GoogleVisionRequest import GoogleVisionRequest
import time

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

class FacialJoyReader:
    google_request = GoogleVisionRequest()
    confidence_threshold = 0.75

    def find_joy_levels(self):
        features = "1:20"
        self.google_request.prepare_picture("capture/funeral2 .jpg", features)
        if (self.google_request.send_picture_to_api()):
            try:
                total_joy = 0
                total_people = 0
                datalist = self.google_request.get_json_datalist()
                print(datalist)

                for responseItem in datalist['responses']:
                    for face_item in responseItem['faceAnnotations']:
                        print (face_item['joyLikelihood'])
                        print (str(get_likelihood_num(face_item['joyLikelihood'])))
                        print(face_item['detectionConfidence'])

                        joy_rating = get_likelihood_num(face_item['joyLikelihood'])
                        confidence = face_item['detectionConfidence']
                        if (confidence >= self.confidence_threshold):
                            total_joy = total_joy + joy_rating
                            total_people = total_people + 1

                print("People with confident facial readings " + str(total_people))
                avg_joy = total_joy / total_people
                print("Average joy " + str(avg_joy))
                print(get_likelihood_type(int(0.5 + avg_joy)))

            except:
                print("Misread")



new_item = FacialJoyReader()
new_item.find_joy_levels()