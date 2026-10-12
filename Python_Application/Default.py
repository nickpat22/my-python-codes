def Area(Radius, PI=3.14):      #Default Argument should be always tranning
    Ans = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(10.5)
    print("Area of Circle is: ", Ret)

    Ret = Area(10.5,7.12)
    print("Area of Circle is: ", Ret)



if __name__ == "__main__":
    main()