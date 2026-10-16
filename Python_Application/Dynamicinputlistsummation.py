def Summation(Data):
    Sum = 0
    for no in Data:
        Sum = Sum + no
    return Sum     


def main():
    size = 0
    Arr = list()

    print("Enter The no of Elements : ")
    size = int(input())

    print("Enter the elements : ")

    for i in range(size):
        no = int(input())
        Arr.append(no)
    ret = Summation(Arr)
    print("Summation is :", ret)

if __name__ == "__main__":
    main()