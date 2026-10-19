def main():
    try:
        fobj = open("Demo.txt","w")
        print("File gets Open")

        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in Current Directory")
if __name__ == "__main__":
    main()