import os
def main():
    for FolderName ,  SubFolder , FileName in os.walk("Marvellous"):
        print("Folder Name : ",FolderName)
        for subf in SubFolder:
            print("SubFolder name : ",subf)

if __name__ == "__main__":
    main()