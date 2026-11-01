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

#----------------------------------------------------------------
#   Function Name : Main
#   Description   : Entry Point Function
#   Input         : None
#   Output        : None
#   Name of Author: Nikunj patidar
#   Date          : 16/08/26
#-----------------------------------------------------------------
def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()