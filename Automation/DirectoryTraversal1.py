import os
def main():
    for FolderName ,  SubFolder , FileName in os.walk("Marvellous"):
        print(FolderName)

if __name__ == "__main__":
    main()