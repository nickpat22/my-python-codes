sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels =  [1,0,0] #sentiments

for sentense , label in zip(sentenses,labels):
    sentiment = "Positive" if label == 1 else "Negative"

    print("Sentence :",sentense)
    print("label :",label)
    print("Sentiment :",sentiment)
    print("-------------------------")

