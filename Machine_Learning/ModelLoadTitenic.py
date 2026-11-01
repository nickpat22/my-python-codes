import pandas as pd
import joblib

def LoadModel(filename):
    model = joblib.load(filename)

    print("Model Loaded Sucessfully")

    print(model.feature_names_in_)

    return model

def PredictPassenger(model):
    print("Enter Information")

    Pclass = int(input("Enter Pclass(1/2/3)"))
    Sex = int(input("Enter Sex (0 - M , 1 : F): "))
    Age = float(input("Enter Age : "))
    sibsp = int(input("Enter sibsp : "))
    Parch = int(input("Enter Parch"))
    Fare = int(input("Enter Fare"))
    Embarked = float(input("Enter Embarked(0/1/2)"))

    passenger = pd.DataFrame([{
        "Pclass" : Pclass,
        "Sex" : Sex,
        "Age" : Age,
        "sibsp":sibsp,
        "Parch":Parch,
        "Fare" : Fare,
        "Embarked_1.0": 1 if Embarked ==1 else 0,
        "Embarked_2.0": 1 if Embarked ==2 else 0,


    }])

    passenger = passenger[model.feature_names_in_]
    result = model.predict(passenger)

    print(result)


def main():
    model = LoadModel("MarvellousTitanic.pkl")
    PredictPassenger(model)

if __name__ == "__main__":
    main()