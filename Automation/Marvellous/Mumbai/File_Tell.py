def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets Open")

        print("File offset is : ",fobj.tell())

        data = fobj.read(10)
        print(data)

        print("File offset is : ",fobj.tell())
        
    except FileNotFoundError as fobj:
        print("File is not present in Current Directory")
if __name__ == "__main__":
    main()