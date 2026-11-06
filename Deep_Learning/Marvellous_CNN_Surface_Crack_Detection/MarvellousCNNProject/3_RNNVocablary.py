sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

vocabluary = []

for sentense in sentenses:
    words = sentense.split()

    for word in words:
        if word not in vocabluary: 
            vocabluary.append(word)

for index, x in enumerate(vocabluary):
    print("Position", index+1,":", x)
