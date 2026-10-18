def filterX(Task,Elements):
    result = list()

    for no in Elements:
        ret = Task(no)

        if Task(no) == True:
            result.append(no)

    return result

def mapX(Task,Elements):
    result = list()

    for no in Elements:
        ret = Task(no)
        result.append(ret)
    
    return result

def reduceX(Task,Elements):
    result = 0

    for no in Elements:
        result = Task(result,no)

    return result

