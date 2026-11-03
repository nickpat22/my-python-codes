import pandas as pd
import matplotlib.pyplot as plt


from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    #Step 1 : Load the Data

    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset loaded with values")

    print(df.head())

    print("Missing Values : ")
    print(df.isnull().sum())

    #Step 2 : Feature Selection

    X = df[["Annual Income (k$)","Spending Score (1-100)"]]

    print("Selected Features :")
    print(X.head())
#Scale the data

    scaller = StandardScaler()

    X_scalled = scaller.fit_transform(X)

    print("Scalled Data : ")
    print(X_scalled[:5])

if __name__ == "__main__":
    main()