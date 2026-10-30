import numpy as np
import pandas as pd
import matplotlib.pylab as plt

def MarvellousPredictor():
    #Lod the Data

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables X : ",X)
    print("Values of Dependent Variables Y : ",Y)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_X = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean_X is :",mean_X)
    print("Mean_Y is :",mean_y)

    



def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()