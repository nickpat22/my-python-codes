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

    print("Data Loaded Succesfully")
    print(df.head())
    return df

# Step 2
#----------------------------------------------------------------
#   Function Name : PreprocessData
#   Description   : It performs data analysis
#   Input         : Data Frame
#   Output        : Updated Data frame
#   Name of Author: Nikunj patidar
#   Date          : 16/08/26
#-----------------------------------------------------------------
def PreprocessData(df):
    df = df.drop(
        columns =[
        "Passengerid",
        "zero",
        "name"
        ],
        errors = "ignore")

    # Handell missing Values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    #Convert  Catogarical to numric data
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first= True,
        dtype=int
    )
    print(df.head())

    print("Data Preprossesing Completed")

    return df

# Step 3
#----------------------------------------------------------------
#   Function Name : Split Data
#   Description   : It performs Spliting Activity
#   Input         : Dataframe
#   Output        : 4 subset for training and testing
#   Name of Author: Nikunj patidar
#   Date          : 16/08/26
#-----------------------------------------------------------------

# Name of Author: Nikunj patidar
# Date          : 16/08/26
# -----------------------------------------------------------------

def SplitData(df):
    X = df.drop("Survived", axis=1)
    Y = df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Dataset Splitting Completed Successfully")

    return X_train, X_test, Y_train, Y_test
# Step 4
#----------------------------------------------------------------
#   Function Name : Train Model
#   Description   : It performs Model Training
#   Input         : Training Features and Lables 
#   Output        : Trained Model
#   Name of Author: Nikunj patidar
#   Date          : 16/08/26
#-----------------------------------------------------------------

def TrainModel(X_train, Y_train):
    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, Y_train)

    print("Model Training Completed Successfully")

    return model


# Step 5
#----------------------------------------------------------------
#   Function Name : Evaulate Model
#   Description   : It performs Model Testing
#   Input         : Model , testing data (features,labels)
#   Output        : None
#   Name of Author: Nikunj patidar
#   Date          : 16/08/26
#-----------------------------------------------------------------

def EvaluateModel(model,X_Test,Y_test):
    Y_pred = model.predict(X_Test)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuricy is ,",accuracy)
    print(confusion_matrix(Y_test,Y_pred))

# Step 6
#----------------------------------------------------------------
#   Function Name : Preserve Model
#   Description   : It performs Model Preservation Into .pkl file
#   Input         : Model
#   Output        : None
#   Name of Author: Nikunj patidar
#   Date          : 16/08/26
#-----------------------------------------------------------------

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model Preserved with name : ",filename)



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

    #step3
    X_train,X_test,Y_train,Y_test = SplitData(df)

    #step4
    Model = TrainModel(X_train,Y_train)

    #step  5
    EvaluateModel(Model,X_test,Y_test)

    #step6
    PreserveModel(Model,"MarvellousTitanic.pkl")


if __name__ == "__main__":
    main()