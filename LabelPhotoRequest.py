import argparse
import base64
import json
import sys
import requests
from SoundControl import SoundControl
from WebCamCapture import WebCamCapture
from GoogleVisionRequest import GoogleVisionRequest
import time

class Label:
    description = ""
    score=0

class ItemOfInterest:
    tag = ""
    tagList = list()
    threshold = 0
    priority = 0
    coolDown = 0
    lastTriggered = 0
    nextTrigger = 0
    audioResponse = ""
    visualResponse = ""

    def setTriggered(self):
        self.lastTriggered = int(time.time())
        self.nextTrigger = self.lastTriggered + self.coolDown

    def matchesLabel(self, labelName, labelScore, currentPriority):
        currentTime = time.time()
        if currentTime > self.coolDown:
            for thisTag in self.tagList:
                if thisTag in labelName:
                    if labelScore > self.threshold:
                        if self.priority < currentPriority:
                            return True
        return False

    def getPriority(self):
        return self.priority

    def triggerResponse(self):
        self.setTriggered()
        soundDisplay = SoundControl()
        soundDisplay.soundAndImageDisplay(self.audioResponse, self.visualResponse, "API Matched Item")

class LabelPhotoRequest:

    labelList = list()
    itemList = list()
    googleRequest = GoogleVisionRequest()



    def takePicture(self):
        self.labelList.clear()
        snapShot = WebCamCapture()
        features = "4:20"

        if (snapShot.pictureCountdown()):
            self.googleRequest.preparePicture(snapShot.getPictureName(), features)
            if (self.googleRequest.sendPictureToAPI()):
                try:
                    dataList = self.googleRequest.getJSONDatalist()

                    for responseItem in dataList['responses']:
                        for labelItem in responseItem['labelAnnotations']:
                            labelDetails = Label()
                            labelDetails.description = labelItem['description']
                            labelDetails.score = labelItem['score']
                            self.labelList.append(labelDetails)

                    print("API Response")
                    for thisThing in self.labelList:
                        print(thisThing.description + " = " + str(thisThing.score))

                    pictureMatch = False
                    currentMatch = ItemOfInterest()
                    currentMatch.priority = 100

                    for visualLabel in self.labelList:
                        for itemOfInterest in self.itemList:
                            if itemOfInterest.matchesLabel(visualLabel.description, visualLabel.score, currentMatch.priority ):
                                currentMatch = itemOfInterest
                                pictureMatch = True

                    if pictureMatch:
                        currentMatch.triggerResponse()
                    else:
                        print ("No match")
                        #snapShot.deletePicture()
                except:
                    soundDisplay = SoundControl()
                    soundDisplay.errorBlip()
                    print("Issue processing data returned from Google Vision API")




