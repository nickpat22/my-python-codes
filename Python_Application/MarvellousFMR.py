CheckEven = lambda No : (No % 2 == 0)
Incriment = lambda No : No+1
Addition = lambda No1,No2 : No1+No2

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        ret = Task(no)      #CheckEven(no)

        if(ret == True):
            Result.append(no)

    return Result

def mapX(Task, Elements):
    Result = list()

    for no in Elements:
        ret = Task(no)          #Incriment

        Result.append(ret)

    return Result

def reduceX(Task,Elements):
    Sum = 0

    for no in Elements:
        Sum = Task(Sum,no)

    return Sum

def main():
    data = [13,12,8,10,11,20]
    print("Input Data is : ", data)

    Fdata = list(filterX(CheckEven,data))

    print("Data afte filter :",Fdata)

    Mdata = list(mapX(Incriment,Fdata))

    print("Data after Map :",data)

    Rdata = reduceX(Addition,Mdata)

    print("Data after reduced is :",Rdata)
    
if __name__ == "__main__":
    main()