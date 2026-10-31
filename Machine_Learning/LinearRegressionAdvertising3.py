import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousRegression(DataPath):

    border = "-"*40
    # Step1: Load the data
    print(border)
    print("# Step1: Load the data")
    print(border)

    df = pd.read_csv(DataPath)
    print(df.head())

    # Step2: Remove Unwanted Columns
    print(border)
    print("Step2: Remove Unwanted Columns")
    print(border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    # Step3: Check Missing Values
    print(border)
    print("Step3: Check Missing Values")
    print(border)

    print(border)
    print("Total missing Values : ")
    print(df.isnull().sum())
    print(border)

    # Step4: Statistical Summary
    print(border)
    print("Step4: Statistical Summary")
    print(border)

    print(df.describe())

    

def main():
    MarvellousRegression("Advertising.csv")
if __name__ == "__main__":
    main()