import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier


#------------------------------------------------------------------------------
#Step 1 : Load the Dataset
#------------------------------------------------------------------------------

df = pd.read_csv("breast_cancer.csv")

print("Shape of Dataset ",df.shape)

print("First few records :")

print(df.head())


#------------------------------------------------------------------------------
#Step 2 : Seperate Features and lables
#------------------------------------------------------------------------------

X = df.drop("target", axis=1)
Y = df["target"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

#------------------------------------------------------------------------------
#Step 3 : Split dataset for training and testing
#------------------------------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#------------------------------------------------------------------------------
#Step 4 : Scale the features
#------------------------------------------------------------------------------

scaller = StandardScaler()

X_train = scaller.fit_transform(X_train)
X_test = scaller.fit_transform(X_test)

#------------------------------------------------------------------------------
#Step 5.1 : Create the Indidual models
#------------------------------------------------------------------------------

model_log = LogisticRegression(max_iter=1000)

model_det = DecisionTreeClassifier(random_state=42)

model_knn = KNeighborsClassifier(n_neighbors=5)

#------------------------------------------------------------------------------
#Step 5.2 : Create the Voating models
#------------------------------------------------------------------------------

model = VotingClassifier(
    estimators=[
        ('logistic',model_log),
        ('desision_tree',model_det),
        ('knn',model_knn)
    ],
    voting='hard'
)

#------------------------------------------------------------------------------
#Step 6 : Train the model
#------------------------------------------------------------------------------

model = model.fit(X_train,Y_train)

#------------------------------------------------------------------------------
#Step 7 : Test the model
#------------------------------------------------------------------------------

y_pred = model.predict(X_test)

#------------------------------------------------------------------------------
#Step 8 : Evaluavte the model
#------------------------------------------------------------------------------

print("Accurecy : ",accuracy_score(Y_test,y_pred))
print("confusion_matrix :")
print(confusion_matrix(Y_test,y_pred))