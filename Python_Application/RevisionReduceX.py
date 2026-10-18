'''from functools import reduce'''
'''from RevisionLibrary import *'''



Checkeven = lambda No : No % 2 == 0
Incriment = lambda No : No + 1
Addition = lambda No1 , No2 : No1 + No2

def filterX(Task, Elements):
    result = list()

    for no in Elements:
        ret = Task(no)

        if (ret == True):
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


def main():
    data = list((13,12,8,10,11,20))
    print("Input Data is : ",data)

    Fdata = list(filterX(Checkeven,data))
    print("Filted Data is",Fdata)

    Mdata = list(mapX(Incriment,Fdata))
    print("Maped Data is : ",Mdata)

    Rdata = reduceX(Addition,Mdata)
    print("Reduced Data is : ",Rdata)





if __name__ == "__main__":
    main()