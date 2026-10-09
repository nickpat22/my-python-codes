# Accept : multiple parameters
# Return : 1 value

def Marvellous(value1, value2):
    print("Inside Marvellous",value1,value2)
    return 21

def main():
    Ret = Marvellous(10, 20)
    print("Return value is: ", Ret)

if __name__ == "__main__":
    main()