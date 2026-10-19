def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets Open")

        data = fobj.read()
        print(data)

    except FileNotFoundError as fobj:
        print("File is not present in Current Directory")
if __name__ == "__main__":
    main()