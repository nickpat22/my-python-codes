import os

def main():

    if (os.path.exists("Demo.txt")):
        print("File is present in current Directory")
    else:
        print("There is no such File")
if __name__ == "__main__":
    main()