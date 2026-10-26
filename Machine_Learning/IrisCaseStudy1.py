from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris Clasification Case Study")
    print("-"*30)
    Dataset = load_iris()
    print(Dataset)

if __name__ == "__main__":
    main()