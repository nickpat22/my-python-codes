#-----------------------------------------------------
# Deep Learning Pipeline
#1. Read the Data from Csv
#2. Data Analysis (EDD)
#3. Preprocessing
#4. TRain Test Split
#5. Feature Scalling
#6. FNN Model Training
#7. Model Evalution
#8. Graphical Repersentation
#9. Model Preserve
#10. Model Loading and preserve
#11.Test unseen Data
#--------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#-----------------------------------------------------
#1. Read the Data from Csv
#-----------------------------------------------------
print("1. Read the Data from Csv")
Data = pd.read_csv("placement_data.csv")
print("Complete Dataset")
print(Data)

#-----------------------------------------------------
#2. Data Analysis (EDD)
#-----------------------------------------------------

print("2. Data Analysis (EDD)")
print("First 5 rows :")
print(Data.head())

print("Columns names : ")
print(Data.columns)

print("Shape of Dataset :")
print(Data.shape)

print("Stastical Summary :")
print(Data.describe())

#-----------------------------------------------------
#3. Preprocessing
#-----------------------------------------------------

print("3. Preprocessing")

X = Data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = Data['Placed']

print("Input Features :")
print(X.head())

print("Target : ")
print(Y.head())

#-----------------------------------------------------
#4. TRain Test Split
#-----------------------------------------------------

print("4. TRain Test Split")

X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.3,random_state=42)

print("Training Input Shape :")
print(X_train.shape)
print("Testing Input Shape :")
print(X_test.shape)
print("Training output Shape :")
print(Y_train.shape)
print("Testing Input Shape :")
print(X_test.shape)

#-----------------------------------------------------
#5. Feature Scalling
#-----------------------------------------------------

print("5. Feature Scaling")

scaller = StandardScaler()

X_train_Scaled = scaller.fit_transform(X_train)
X_test_Scaled = scaller.fit_transform(X_test)

print("Scalled Training data : ")
print(X_train_Scaled[:5])

#-----------------------------------------------------
#6. FNN Model Training
#-----------------------------------------------------

print("6. FNN Model Training")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

print(model)

print("Train The Model :")
model.fit(X_train_Scaled,Y_train)
print("Model Training Completed")

#-----------------------------------------------------
#7. Model Evalution
#-----------------------------------------------------
print("7. Model Evalution")

Y_pred = model.predict(X_test_Scaled)

accuracy = accuracy_score(Y_test,Y_pred)

cm = confusion_matrix(Y_test,Y_pred)

print("Accuracy is :",accuracy)
print("Confusion Matrix is :",cm)

print("Predict The Probablity :")

Y_prob = model.predict_proba(X_test_Scaled)
print(Y_prob[:5])

#-----------------------------------------------------
#9. Model Preserve
#-----------------------------------------------------
print("9. Model Preserve")

joblib.dump(model,"Placement_fnn_model.pkl")
joblib.dump(scaller,"Placement_scaller.pkl")

print("Model and Scaller gets Dumped Sucessfully")

#-----------------------------------------------------
#10. Model Loading and preserve
#-----------------------------------------------------

print("10. Model Loading and preserve")

loaded_model = joblib.load("Placement_fnn_model.pkl")
loaded_scaller = joblib.load("Placement_scaller.pkl")

print("Model gets Loaded Sucessfully")

#-----------------------------------------------------
#11.Test unseen Data
#Aptitude       :70
#coading        :75
#communication  :80
#academics      :85
#Internship     :1
#-----------------------------------------------------
print("11.Test unseen Data")

new_student = pd.DataFrame([[70,75,80,85,1]], columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scalled = loaded_scaller.transform(new_student)     ###

new_prediction = loaded_model.predict(new_student_scalled)

new_probablity = loaded_model.predict_proba(new_student_scalled)

print("New Students Data :")
print(new_student)

print("pridiction Probablity : ",new_probablity)

if new_prediction[0] ==1:
    print("Pridiction: Placed")
else:
    print("Prediction : Unplased")