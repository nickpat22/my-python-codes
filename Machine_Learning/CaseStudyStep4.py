import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

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
print("Step 3 : Visualation of Dataset")
print(Border)

#Scatter plot
plt.figure(figsize=(7,5))

for sp in df["Species"].unique():
    temp = df[df["Species"] == sp]
    plt.scatter(temp["PetalLengthCm"], temp["PetalWidthCm"],lable = sp) #here error

plt.title("Marvellous Iris Case Study")

plt.xlabel("PetalLengthCm")
plt.xlabel("PetalWidthCm")

plt.legend()
plt.grid()
plt.show()
