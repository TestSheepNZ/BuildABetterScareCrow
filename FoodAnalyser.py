import argparse
import base64
import json
import sys
import requests
from LabelPhotoRequest import LabelPhotoRequest, Label, ItemOfInterest

visionRequest = LabelPhotoRequest()

def initialiseFoodItems():
    LabelPhotoRequest.itemList.clear()
    baseThreshold = 0.4

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("crow")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 1
    itemToCheck.audioResponse = "sounds/crow.wav"
    itemToCheck.visualResponse = "images/crow.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("bird")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 5
    itemToCheck.audioResponse = "sounds/bird.wav"
    itemToCheck.visualResponse = "images/bird.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("banana")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 10
    itemToCheck.audioResponse = "sounds/banana.wav"
    itemToCheck.visualResponse = "images/banana.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("apple")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 20
    itemToCheck.audioResponse = "sounds/apple.wav"
    itemToCheck.visualResponse = "images/apple.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("tangerine")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 22
    itemToCheck.audioResponse = "sounds/tangerine.wav"
    itemToCheck.visualResponse = "images/orange.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("mandarin")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 22
    itemToCheck.audioResponse = "sounds/mandarin.wav"
    itemToCheck.visualResponse = "images/orange.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("orange")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 24
    itemToCheck.audioResponse = "sounds/orange.wav"
    itemToCheck.visualResponse = "images/orange.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("kiwi")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 25
    itemToCheck.audioResponse = "sounds/kiwi.wav"
    itemToCheck.visualResponse = "images/kiwi.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("mango")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 22
    itemToCheck.audioResponse = "sounds/mango.wav"
    itemToCheck.visualResponse = "images/mango.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("fruit")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 50
    itemToCheck.audioResponse = "sounds/fruit.wav"
    itemToCheck.visualResponse = "images/fruit.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("food")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 60
    itemToCheck.audioResponse = "sounds/food.wav"
    itemToCheck.visualResponse = "images/food.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("produce")
    itemToCheck.tagList.append("vegetable")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 60
    itemToCheck.audioResponse = "sounds/vegetable.wav"
    itemToCheck.visualResponse = "images/fruit.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("cup")
    itemToCheck.tagList.append("drink")
    itemToCheck.tagList.append("coffee")
    itemToCheck.tagList.append("tea")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 65
    itemToCheck.audioResponse = "sounds/cup.wav"
    itemToCheck.visualResponse = "images/cup.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("pen")
    itemToCheck.tagList.append("pencil")
    itemToCheck.tagList.append("office supplies")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 80
    itemToCheck.audioResponse = "sounds/pen.wav"
    itemToCheck.visualResponse = "images/pen.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("utensil")
    itemToCheck.tagList.append("cutlery")
    itemToCheck.tagList.append("knife")
    itemToCheck.tagList.append("fork")
    itemToCheck.tagList.append("spoon")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 75
    itemToCheck.audioResponse = "sounds/forks.wav"
    itemToCheck.visualResponse = "images/forks.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)

    itemToCheck = ItemOfInterest()
    itemToCheck.tagList = list()
    itemToCheck.tagList.append("human")
    itemToCheck.tagList.append("man")
    itemToCheck.tagList.append("woman")
    itemToCheck.tagList.append("boy")
    itemToCheck.tagList.append("girl")
    itemToCheck.tagList.append("people")
    itemToCheck.tagList.append("person")
    itemToCheck.threshold = baseThreshold
    itemToCheck.priority = 95
    itemToCheck.audioResponse = "sounds/human.wav"
    itemToCheck.visualResponse = "images/human.jpg"
    LabelPhotoRequest.itemList.append(itemToCheck)


initialiseFoodItems()
visionRequest.takePicture()