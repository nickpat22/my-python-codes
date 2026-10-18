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