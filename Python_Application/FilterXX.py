CheckEven = lambda No : (No % 2 == 0)

def main():
    data = [13,12,8,10,11,20]
    print("Input Data is : ", data)

    Fdata = list(filter(CheckEven,data))

    print("Data afte filter :",Fdata)
if __name__ == "__main__":
    main()