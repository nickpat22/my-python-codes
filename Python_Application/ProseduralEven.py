def CheckEven(No):
    if(No % 2 == 0):
        print("Its Even Number")

    else :
        print("Its odd number :")

def main():
    value = int(input("Enter Number : "))
    CheckEven(value)    

if __name__ == "__main__":
    main()