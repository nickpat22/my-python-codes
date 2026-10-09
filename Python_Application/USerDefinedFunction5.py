# Accept : multiple parameters
# Return : multiple value

def Marvellous(value1, value2):
    print("Inside Marvellous",value1,value2)
    return 21, 51

def main():
    Ret1, Ret2 = Marvellous(10, 20)
    print("Return values are: ", Ret1, Ret2)

if __name__ == "__main__":
    main()