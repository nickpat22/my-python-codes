from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris Clasification Case Study")
    print("-"*30)
    Dataset = load_iris()

    # Meta data of dataset
    print("Indipendent Variables are :")
    print(Dataset.feature_names)

    print("Dependent Variables are :")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()