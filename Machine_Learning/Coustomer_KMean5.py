import pandas as pd
import matplotlib.pyplot as plt


from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    #Step 1 : Load the Data

    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset loaded with values")

    print(df.head())

    print("Missing Values : ")
    print(df.isnull().sum())

    #Step 2 : Feature Selection

    X = df[["Annual Income (k$)","Spending Score (1-100)"]]

    print("Selected Features :")
    print(X.head())
#Scale the data

    scaller = StandardScaler()

    X_scalled = scaller.fit_transform(X)

    print("Scalled Data : ")
    print(X_scalled[:5])

#Step 4: elbo method

    WCSS = []

    for k in range(1,11):
        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(X_scalled)
        WCSS.append(model.inertia_)

    print("Values : ")
    for i in range(len(WCSS)):
        print(f"{i+1} : {WCSS[i]}")

# Step 5 :  visulation

    plt.plot(range(1,11),WCSS,marker = "o")
    plt.xlabel("Number of clusters : k")
    plt.ylabel("WCSS")
    plt.title("MArvellous Elbo method analysis")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()