import math
import numpy as np

def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2+(P1['Y'] - P2['Y'])**2)
    return Ans

def MarvellousKNNClassifier():
    Border = "-"*30

    Data = [
        {'point' : 'A','X':1,'Y':2,'label':'Red'},
        {'point' : 'B','X':2,'Y':3,'label':'Red'},
        {'point' : 'C','X':3,'Y':1,'label':'Blue'},
        {'point' : 'D','X':5,'Y':6,'label':'Blue'}
    ]

    print(Border)
    print("Marvellous KNN Classifier")
    print(Border)

    for i in Data:
        print(i)
    print(Border)

    new_point = {'X':3, 'Y':3}

    print("Distences of all points : ")
    print(Border)
    for d in Data:
        d['distance'] = MarvellousEucDistance(d,new_point)

    for d in Data:
        print(d)

    print(Border)

    sorted_data = sorted(Data, key= lambda item : item['distance'])

    print(Border)
    print("Sorted Data : ")
    for d in sorted_data:
        print(d)
    print(Border)

    k = 3

    nearest = sorted_data[:k]       #imp
    print(Border)
    print("Nearest 3 Members are : ")
    print(Border)

    for d in nearest:
        print(d)

    print(Border)

    # voting

    votes = {}

    for neighbours in nearest:
        label = neighbours['label']
        votes[label] = votes.get(label,0) + 1

    print(Border)
    print("Voting Result is : ")
    print(Border)

    for d in votes:
        print("Name:",d,"Number of votes :",votes[d])

    print(Border)

    iMax = 0 
    Name = ""
    for d in votes:
        if( votes[d] > iMax):
            iMax = votes[d]
            Name = d

    print("Final pridication is :", Name)


def main():
    MarvellousKNNClassifier()



if __name__ =="__main__":
    main()