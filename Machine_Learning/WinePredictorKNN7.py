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

     #Step 3 : Seperate indipendent and dependent Variables
    print(Border)
    print("#Step 3 : Seperate indipendent and dependent Variables")
    print(Border)

    X = df.drop(columns=['class_label']) #class_label sodun baki che
    Y = df['class_label']

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)
    print("Input Columns : ", X.columns.tolist())
    print("Output Column : class_label")
    print(Border)

     #Step 4 : Split the Dataset for training and testing
    print(Border)
    print("Step 4 : Split the Dataset for training and testing")
    print(Border)

    X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Border)
    print("Details of training and testing data")

    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)

    print(Border)

     #Step 5 : Feature Scalling
    print(Border)
    print("Step 5 : Feature Scalling")
    print(Border)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature Scaling donr")
    print(Border)

    # Step 6 : HyperParameter Tuning

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors= k)
        model = model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)

        accuracy_scores.append(accuracy)

    print("Accuracy Report : ")
    for no in accuracy_scores:
        print(no)

    print(Border)

    print(Border)
    print("Graphical Representation : ")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = "o")
    plt.title("K Values VS accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()




def main():
    MarvellousClassifier("wine_data.csv")

if __name__ == "__main__":
    main()