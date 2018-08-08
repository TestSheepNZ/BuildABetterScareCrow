import argparse
import base64
import json
import sys
import requests
from SoundControl import SoundControl
from WebCamCapture import WebCamCapture
import time

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
    projectAPIKey = "USE YOUR OWN KEY PLEASE"
    dataList = ""


    def preparePicture(self, imageFilename, features):

        request_list = []
        with open(imageFilename, 'rb') as image_file:
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

    def getJSONDatalist(self):
        return self.dataList

    def sendPictureToAPI(self):
        try:
            data = open(self.output_filename)


            urlRequest = "https://vision.googleapis.com/v1/images:annotate?key=" + self.projectAPIKey
            print(urlRequest)
            response = requests.post(url=urlRequest,
                                     data=data,
                                     headers={'Content-Type': 'application/json'})
            self.dataList = response.json()


            return True
        except:
            soundDisplay = SoundControl()
            soundDisplay.errorBlip()
            print("Error with response from Google Vision API")
            return False


