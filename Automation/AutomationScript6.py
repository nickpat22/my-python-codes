import sys

def main():
    Border = "-"*60
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)
    if (len(sys.argv) == 2):
        if(sys.argv[1] =="--h" or sys.argv[1] =="--H"):
            print("This automation Script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectorryName Should be absolute path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory Name is : ",DirectoryName)
    else:

        print("Invalid No of argument")
        print("Please use --h or --u for more information")
    
    print(Border)
    print(" Thank you Marvellous Automation Script ")
    print(Border)
if __name__ == "__main__":
    main()