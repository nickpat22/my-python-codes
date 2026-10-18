CheckEven = lambda No : (No % 2 == 0)
        
def main():
    value = int(input("Enter Number : "))
    Ret = CheckEven(value)     # Ret =(Value % 2 == 0)

    if(Ret == True):
        print("Its even number")

    if(Ret == False):
        print("Its odd number")

if __name__ == "__main__":
    main()       