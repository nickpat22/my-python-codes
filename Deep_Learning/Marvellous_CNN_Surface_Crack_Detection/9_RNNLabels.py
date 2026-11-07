sentenses = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels =  [1,0,0] #sentiments

for sentense , label in zip(sentenses,labels):
    print("Sentence :",sentense)
    print("label :",label)

    if label == 1:
        print("Meaning Postive Sentiment")
    else:
        print("Meaning : Negative sentiment")
        
    print("-------------------------")

