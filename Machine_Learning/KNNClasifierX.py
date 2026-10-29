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

    print("Indipendent Variables are : ")
    print(X)

    print("Dependent Variables are :")
    print(Y)

    print("Testing point is :")
    print(new_point)


if __name__ =="__main__":
    main()