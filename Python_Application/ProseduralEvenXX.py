def CheckEven(No):
    if(No % 2 == 0):
        return True

    else :
        return False

def main():
    value = int(input("Enter Number : "))
    Ret = CheckEven(value)

    if(Ret == True):
        print("Its even number")

    if(Ret == False):
        print("Its odd number")

if __name__ == "__main__":
    main()       