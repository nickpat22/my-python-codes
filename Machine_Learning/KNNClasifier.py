import numpy as np
from sklearn.neighbors import KNeighborsClassifier



def main():
    #indipendent
    X = np.array([
        [1,2],
        [2,3],
        [3,1],
        [5,6]
    ])
    #dependent
    Y = np.array([
        ["Red"],
        ["Red"],
        ["Blue"],
        ["Blue"]
    ])

    new_point = np.array([[3,3]])

    #Model Creation
    model = KNeighborsClassifier(n_neighbors=3)
    model = model.fit(X,Y)

    Y_pred = model.predict(new_point)

    print("Predicted lable : ",Y_pred)


if __name__ =="__main__":
    main()