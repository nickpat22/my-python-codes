import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    Border = "-"*40

    #Step 1: Load the dataset from csv file
    print(Border)
    print("Step 1: Load the dataset from csv file")
    print(Border)

    df = pd.read_csv(DataPath)
    print(Border)
    print("Some entries from dataset :")
    print(df.head())
    print(Border)

    #Step 2 : Clean the Dataset
    print(Border)
    print("#Step 2 : Clean the Dataset")
    print(Border)

    df.dropna(inplace=True)

    print("Shape of Dataset : ",df.shape)
    print("Total records : ",df.shape[0])
    print("Total Column : ", df.shape[1])


def main():
    MarvellousClassifier("wine_data.csv")

if __name__ == "__main__":
    main()