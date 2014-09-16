STORE_ITEMS = {
    "gift_card": {
        "returnable" : False,
        "title" : "Gift Card",
        "description" : "Points rewarded for quizzes and tests",
        "shown" : False,
    },
    "brain_sticker": {
        "description": "This sticker has a picture of a brain on it, to celebrate how smart you are!",
        "title": "Brain Sticker",
        "resource_id": "",
        "cost": 5,
        "returnable": False,
        "thumbnail": "data:image/jpeg;base64,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",
        "resource_type": "",
    },
    "pencil": {
        "description": "This is a beautiful pencil that you can buy.",
        "title": "Coloured Pencil",
        "resource_id": "",
        "cost": 10,
        "returnable": False,
        "thumbnail": "data:image/jpeg;base64,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",
        "resource_type": ""
    },
}