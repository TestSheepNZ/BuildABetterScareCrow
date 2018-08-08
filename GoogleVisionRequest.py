import base64
import json
import requests
from SoundControl import SoundControl

DETECTION_TYPES = [
    'TYPE_UNSPECIFIED',
    'FACE_DETECTION',
    'LANDMARK_DETECTION',
    'LOGO_DETECTION',
    'LABEL_DETECTION',
    'TEXT_DETECTION',
    'SAFE_SEARCH_DETECTION',
]


def get_detection_type(detect_num):
    """Return the Vision API symbol corresponding to the given number."""
    detect_num = int(detect_num)
    if 0 < detect_num < len(DETECTION_TYPES):
        return DETECTION_TYPES[detect_num]
    else:
        return DETECTION_TYPES[0]


class GoogleVisionRequest:
    response = ""
    output_filename = "capture/json_image.json"
    project_api_key = ""
    datalist = ""

    def prepare_picture(self, image_filename, features):

        request_list = []
        with open(image_filename, 'rb') as image_file:
            content_json_obj = {
                'content': base64.b64encode(image_file.read()).decode('UTF-8')
            }

        feature_json_obj = []
        for word in features.split(' '):
            feature, max_results = word.split(':', 1)
            feature_json_obj.append({
                'type': get_detection_type(feature),
                'maxResults': int(max_results),
            })

        request_list.append({
            'features': feature_json_obj,
            'image': content_json_obj,
        })

        with open(self.output_filename, 'w') as output_file:
            json.dump({'requests': request_list}, output_file)

    def get_json_datalist(self):
        return self.datalist

    def send_picture_to_api(self):
        try:
            data = open(self.output_filename)

            url_request = "https://vision.googleapis.com/v1/images:annotate?key=" + self.project_api_key
            print(url_request)
            response = requests.post(url=url_request,
                                     data=data,
                                     headers={'Content-Type': 'application/json'})
            self.datalist = response.json()
            return True
        except:
            sound_display = SoundControl()
            sound_display.error_blip()
            print("Error with response from Google Vision API")
            return False
