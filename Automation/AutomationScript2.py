import sys

def main():

    if (len(sys.argv) == 2):
        DirectoryName = sys.argv[1]
        print("Directory Name is : ",DirectoryName)
    else:
        print("Invalid number of arguments")
if __name__ == "__main__":
    main()