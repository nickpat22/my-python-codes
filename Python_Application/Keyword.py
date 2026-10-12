def Area(Radius, PI):
    Ans = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(PI = 3.14, Radius = 10.5)
    print("Area of Circle is: ", Ret)

    '''Ret = Area(13.6,7.12)
    print("Area of Circle is: ", Ret)'''



if __name__ == "__main__":
    main()