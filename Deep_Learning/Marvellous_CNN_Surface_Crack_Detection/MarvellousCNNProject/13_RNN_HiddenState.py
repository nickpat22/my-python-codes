words = ["food","was","not","good"]

hidden_state = "empty memory"

print("Input tokens :",words)

print("Initial Hidden State :",hidden_state)

for index,word in enumerate(words):
    print("TimeStamp :",index+1)
    print("Current Word :",word)
    print("Priveious Memory :",hidden_state)

    hidden_state = "Memory afte Reading" + "".join(words[index + 1]) + ""

    print("Upadted Memory : ",hidden_state)
    print('-'*30)