def main():
    try:
        fobj = open("Demo.txt","a")
        print("File gets Open")

        fobj.write(" Pune Maharashtra")
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in Current Directory")
if __name__ == "__main__":
    main()