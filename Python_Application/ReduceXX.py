from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

Incriment = lambda No : No+1

Addition = lambda No1,No2 : No1+No2

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