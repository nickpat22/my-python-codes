from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


# Study_Hours, Attendence, Assignment_Score
X = [
    [1,40,30],
    [2,50,35],
    [3,60,40],
    [4,65,50],
    [5,70,55],
    [6,75,65],
    [7,80,70],
    [2,45,25],
    [8,90,85],
    [1,35,20],
    [3,55,20],
    [4,65,50],
    [5,70,55],
    [6,75,60],
    [7,85,75]
]

Y = [0,0,0,1,1,1,1,0,1,0,0,1,1,1,1]

X_train,X_test,Y_tarin,Y_test =train_test_split(X,Y,test_size=0.3,random_state=42)

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42 
)

model = model.fit(X_train,Y_tarin)

Y_pred = model.predict(X_test)

print("Actual Output : ",Y_test)
print("Predicted Output :",Y_pred)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of Deep LEarning Model is : ", accuracy)