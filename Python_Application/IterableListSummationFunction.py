def Summation(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum

def main():
    Marks = [78,90,56,98,77] 

    ret = Summation(Marks)
    
    print("Addition is : ",ret) 

if __name__ == "__main__":
    main()