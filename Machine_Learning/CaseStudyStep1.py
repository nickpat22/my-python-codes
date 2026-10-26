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