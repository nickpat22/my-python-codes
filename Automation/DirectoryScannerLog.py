import sys
import os

def DirectoryScanner(DirectoryPath):

    fobj = open("MarvellousLog.txt","w")

    fobj.write(" Marvellous Automation Script \n")

    fobj.write("Files From The Directory Are : \n")
    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname+"\n")
    fobj.close

def main():
    Border = "-" * 40
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to traverse the directory.")
            print("For better usage please check --u flag")
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Please execute the script as:")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be an absolute path.")
        else:
            DirectoryName = sys.argv[1]
            DirectoryScanner(DirectoryName)
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print(" Thank you for using Marvellous Automation Script ")
    print(Border)

if __name__ == "__main__":
    main()