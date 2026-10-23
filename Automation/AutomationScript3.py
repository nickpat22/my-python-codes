# python Autionation.py --h
# python Autionation.py --u
# python Autionation.py Marvellous

# python Autionation.py --d
# python Autionation.py Marvellous Demo

import sys

def main():

    if (len(sys.argv) == 2):
        if(sys.argv[1] =="--h" or sys.argv[1] =="--H"):
            print("Help")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage")
        else:
            DirectoryName = sys.argv[1]
            print("Diirectory Name is :",DirectoryName)
    else:
        print("Invalid No of argument")
        print("Please use --h or --u for more information")
if __name__ == "__main__":
    main()