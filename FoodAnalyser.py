from LabelPhotoRequest import LabelPhotoRequest, Label, ItemOfInterest

vision_request = LabelPhotoRequest()


def initialise_food_items():
    vision_request.item_list.clear()
    base_threshold = 0.4

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("crow")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 1
    item_to_check.audio_response = "sounds/crow.wav"
    item_to_check.visual_response = "images/crow.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("bird")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 5
    item_to_check.audio_response = "sounds/bird.wav"
    item_to_check.visual_response = "images/bird.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("banana")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 10
    item_to_check.audio_response = "sounds/banana.wav"
    item_to_check.visual_response = "images/banana.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("apple")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 20
    item_to_check.audio_response = "sounds/apple.wav"
    item_to_check.visual_response = "images/apple.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("tangerine")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 22
    item_to_check.audio_response = "sounds/tangerine.wav"
    item_to_check.visual_response = "images/orange.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("mandarin")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 22
    item_to_check.audio_response = "sounds/mandarin.wav"
    item_to_check.visual_response = "images/orange.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("orange")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 24
    item_to_check.audio_response = "sounds/orange.wav"
    item_to_check.visual_response = "images/orange.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("kiwi")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 25
    item_to_check.audio_response = "sounds/kiwi.wav"
    item_to_check.visual_response = "images/kiwi.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("mango")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 22
    item_to_check.audio_response = "sounds/mango.wav"
    item_to_check.visual_response = "images/mango.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("fruit")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 50
    item_to_check.audio_response = "sounds/fruit.wav"
    item_to_check.visual_response = "images/fruit.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("food")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 60
    item_to_check.audio_response = "sounds/food.wav"
    item_to_check.visual_response = "images/food.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("produce")
    item_to_check.tag_list.append("vegetable")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 60
    item_to_check.audio_response = "sounds/vegetable.wav"
    item_to_check.visual_response = "images/fruit.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("cup")
    item_to_check.tag_list.append("drink")
    item_to_check.tag_list.append("coffee")
    item_to_check.tag_list.append("tea")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 65
    item_to_check.audio_response = "sounds/cup.wav"
    item_to_check.visual_response = "images/cup.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("pen")
    item_to_check.tag_list.append("pencil")
    item_to_check.tag_list.append("office supplies")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 80
    item_to_check.audio_response = "sounds/pen.wav"
    item_to_check.visual_response = "images/pen.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("utensil")
    item_to_check.tag_list.append("cutlery")
    item_to_check.tag_list.append("knife")
    item_to_check.tag_list.append("fork")
    item_to_check.tag_list.append("spoon")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 75
    item_to_check.audio_response = "sounds/forks.wav"
    item_to_check.visual_response = "images/forks.jpg"
    vision_request.item_list.append(item_to_check)

    item_to_check = ItemOfInterest()
    item_to_check.tag_list = list()
    item_to_check.tag_list.append("human")
    item_to_check.tag_list.append("man")
    item_to_check.tag_list.append("woman")
    item_to_check.tag_list.append("boy")
    item_to_check.tag_list.append("girl")
    item_to_check.tag_list.append("people")
    item_to_check.tag_list.append("person")
    item_to_check.threshold = base_threshold
    item_to_check.priority = 95
    item_to_check.audio_response = "sounds/human.wav"
    item_to_check.visual_response = "images/human.jpg"
    vision_request.item_list.append(item_to_check)


initialise_food_items()
vision_request.take_picture()