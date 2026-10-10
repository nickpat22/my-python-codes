def BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amule Icecreame Parlor")

def main():             #allowed
    BigBazar()       
    Amul()                 #Error
    BigBazar.Amul()     #Error

if __name__ == "__main__":
    main()