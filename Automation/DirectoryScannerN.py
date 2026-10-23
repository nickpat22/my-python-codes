import sys
import os
def DirectoryScanner(DirectoryPath):
    print("Files From The Directory Are:")

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            print(fname)

def main():
    Border = "-" * 50
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)
    if len(sys.argv) == 2:
        if(sys.argv[1] =="--h" or sys.argv[1] =="--H"):
            print("This automation Script is used to travel the directory")
            print("For better usage please check --u flag")
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Please execute the script as:")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be an absolute path.")
        else:
            DirectoryName = sys.argv[1]
            print("The directory Name is:",DirectoryName)
            DirectoryScanner(DirectoryName)
    else:
        print("Invalid No of argument")
        print("Please use --h or --u for more information")

    print(Border)
    print(" Thank you for using Marvellous Automation Script ")
    print(Border)
if __name__ == "__main__":
    main()