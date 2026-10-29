import pandas as pd

def main():
    sobj = pd.Series([11,21,51,101],index = ["c","C++","Java","Python"])

    print(sobj)

    print(sobj["Python"])

if __name__ ==  "__main__":
    main()