import pandas as pd 
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

#Step 1: Load Data
#----------------------------------------------------------------
#   Function Name : LoadData
#   Description   : Load the Data from CSV
#   Input         : Name of Csv file
#   Output        : Data frame
#   Name of Author: Nikunj Patidar
#   Date          : 16/08/26
#-----------------------------------------------------------------
def LoadData(filename):
    df = pd.read_csv(filename)

    print("Data Loaded")

    return df

# Step 2
#----------------------------------------------------------------
#   Function Name : Main
#   Description   : Entry Point Function
#   Input         : None
#   Output        : None
#   Name of Author: Nikunj patidar
#   Date          : 16/08/26
#-----------------------------------------------------------------
def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
        ],
        errors = "ignore"
        )

    # Handell missing Values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    #convert  Catogarical to numric
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first= True,
        dtype=int
    )
    print(df.head())

    print("Data Preprossesing Completed")

    return df


#----------------------------------------------------------------
#   Function Name : Main
#   Description   : Entry Point Function
#   Input         : None
#   Output        : None
#   Name of Author: Nikunj patidar
#   Date          : 16/08/26
#-----------------------------------------------------------------




def main():
    #step 1 :
    df = LoadData("MarvellousTitanicDataset.csv")

    #Step 2  
    df = PreprocessData(df)


if __name__ == "__main__":
    main()