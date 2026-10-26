import pandas as pd

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

