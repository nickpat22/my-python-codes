import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

Border = "-"*30

###############################################################
# Step 1 : Load the Dataset
################################################################


print(Border)
print("# Step 1 : Load the Dataset")
print(Border)

DataPath = "Iris.csv"

df = pd.read_csv(DataPath)  #Reads all data

print("Dataset Loaded Succesfully")

print("Initial Entries from dataset are :")
print(df.head())

###############################################################
# Step 2 : Data Analysis (EDA)
################################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of Dataset : ",df.shape)
print("Column names : ",list(df.columns))

print("Missing values per column : ")
print(df.isnull().sum())

print("Class Distribution (Species count)")
print(df["Species"].value_counts())

print("Statistical report of dataset : ")
print(df.describe())

###############################################################
# Step 3 : Deside independent and dependent variables
################################################################

print(Border)
print("Step 3 : Deside independent and dependent variables")
print(Border)

# X : Independent Variable / features
# Y : Dependent variables / lables

feature_cole = [
    "SepalLengthCm",
    "SepalWidthCm",
    "PetalLengthCm",
    "PetalWidthCm"
    ]

X = df[feature_cole]
Y = df["Species"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

###############################################################
# Step 4 : Visualation of Dataset
################################################################

print(Border)
print("Step 4 : Visualation of Dataset")
print(Border)

#Scatter plot
plt.figure(figsize=(7,5))

for sp in df["Species"].unique():
    temp = df[df["Species"] == sp]
    plt.scatter(temp["PetalLengthCm"], temp["PetalWidthCm"],label = sp) #here error

plt.title("Marvellous Iris Case Study")

plt.xlabel("PetalLengthCm")
plt.xlabel("PetalWidthCm")

plt.legend()
plt.grid()
plt.show()

###############################################################
# Step 5 : Split the dataset for training and testing
################################################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.5, random_state = 42)

print("Dtataset Spliting Activity Done")

print("X :",X.shape)    #(150,4)
print("Y :",Y.shape)    #(150,)

print("X_train : ",X_train.shape)  #(75,4)
print("X_test : ",X_test.shape)     #(75,4)

print("Y_train : ",Y_train.shape)   #(75,)
print("Y_test : ",Y_test.shape)   #(75,)

###############################################################
# Step 6 : Build the Model
################################################################

print(Border)
print("Step 6 : Build the Model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model Gets Created Sucessfully")

###############################################################
# Step 7 : Train the Model
################################################################

print(Border)
print("Step 7 : Train the Model")
print(Border)

model.fit(X_train,Y_train)

print("Model Trained Successfully")