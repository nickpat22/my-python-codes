import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    X = np.array([[1],[2],[3],[4],[5]])

    Y = np.array([50,55,60,65,70])

    Model = LinearRegression()

    Model = Model.fit(X,Y)

    print(Model.predict([[6]]))

if __name__ == "__main__":
    main()