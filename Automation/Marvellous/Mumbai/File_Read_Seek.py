#seek(Kuthe,Kuthun)


def main():
    try:
        
        fobj = open("Demo.txt","r")
        print("File gets Open")

        fobj.seek(10,0)

        Data = fobj.read()
        print(Data)
        
    except FileNotFoundError as fobj:
        print("File is not present in Current Directory")
if __name__ == "__main__":
    main()


    