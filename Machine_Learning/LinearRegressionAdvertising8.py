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

    # Step5: Correlation
    print(border)
    print("Correlation")
    print(border)

    print(df.corr())       #correlation Matrix  #df = dataframe

    # Step6: Seperate Independent and Dependent Varibles
    print(border)
    print("Step6: Seperate Independent and Dependent Varibles")
    print(border)

    X = df[["TV","radio","newspaper"]] 
    Y = df["sales"]

    print("Indipendent variables :")
    print(X.head())

    print("Dipendent variables :")
    print(Y.head())

  # Step7: Split the Dataset
    print(border)
    print("Step7: Split the Dataset")
    print(border)

    x_train,x_test,y_tarin,y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data : ",x_train.shape)
    print("Testing Data : ",x_test.shape)

  # Step8: Create and train the Model
    print(border)
    print("Step8: Create and train the Model")
    print(border)

    model = LinearRegression()

    model = model.fit(x_train,y_tarin)
    print("Model Trained Sucessfully")

  # Step9: Test the Model
    print(border)
    print("Step9: Test the Model")
    print(border)

    y_pred = model.predict(x_test)
    
    print("Expected Answers : ")
    print(y_test[:3])

    print("Pridicted Answers : ")
    print(y_pred[:3])

  # Step10: Evauluate the Model
    print(border)
    print("Step10: Evauluate the Model")
    print(border)

    MSE = mean_squared_error(y_test,y_pred) #Mean Square Error
    RMSE = np.sqrt(MSE)                     #Root Mean Square Error
    R2 = r2_score(y_test,y_pred)

    print("MSE : ",MSE)
    print("RMSE : ",RMSE)
    print("R2 : ",R2)

    # Step11: Display Coefficient
    print(border)
    print("Step11: Display Coefficient")
    print(border)


    print("TV Coefficient : ",model.coef_[0])   #TV
    print("Radio Coefficient : ",model.coef_[1]) #Radio
    print("NewsPaper Coefficient : ",model.coef_[2])  #Newspaper


    print("Intersept : ",model.intercept_)





def main():
    MarvellousRegression("Advertising.csv")
if __name__ == "__main__":
    main()