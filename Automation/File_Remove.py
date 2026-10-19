import os

def main():
    try:
        # fobj.reomove -> not applicable
        os.remove("Demo.txt")
        

    except FileNotFoundError as fobj:
        print("File is not present in Current Directory")
if __name__ == "__main__":
    main()