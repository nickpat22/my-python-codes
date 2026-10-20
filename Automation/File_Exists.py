import os

def main():
    ret = os.path.exists("Demo.txt")

    if (ret == True):
        print("File is present in current Directory")
    else:
        print("There is no such File")
if __name__ == "__main__":
    main()