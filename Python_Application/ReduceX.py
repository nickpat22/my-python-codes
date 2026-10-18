from functools import reduce

def CheckEven(No):
    return(No % 2 == 0)

def Incriment(No):
    return No + 1

def Addition(No1,No2):
    return No1 + No2

def main():
    data = [13,12,8,10,11,20]
    print("Input Data is : ", data)

    Fdata = list(filter(CheckEven,data))

    print("Data afte filter :",Fdata)

    Mdata = list(map(Incriment,Fdata))

    print("Data after Map :",data)

    Rdata = reduce(Addition,Mdata)

    print("Data after reduced is :",Rdata)

if __name__ == "__main__":
    main()