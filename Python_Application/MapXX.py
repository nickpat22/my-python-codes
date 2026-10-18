CheckEven = lambda No : (No % 2 == 0)

Incriment = lambda No: (No + 1)

def main():
    data = [13,12,8,10,11,20]
    print("Input Data is : ", data)

    Fdata = list(filter(CheckEven,data))

    print("Data afte filter :",Fdata)

    Mdata = list(map(Incriment,data))

    print("Data after Map :",Mdata)
if __name__ == "__main__":
    main()