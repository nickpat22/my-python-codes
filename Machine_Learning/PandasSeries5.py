import pandas as pd

def main():
    sobj = pd.Series([11,21,51,101],index = [5,6,7,8])

    print(sobj)

    print(sobj[7])

if __name__ ==  "__main__":
    main()