import sys
import os
import time
import schedule


def DirectoryScanner(DirectoryPath="Marvellous"):
    Border = "_" * 40
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_") 

    print("Log File Gets Created With Name :", LogFileName)

    fobj = open(LogFileName,"w")
    fobj.write(Border+"\n")
    fobj.write("MARVELLOUS AUTOMATION SCRIPT\n")
    fobj.write(Border+"\n")
    fobj.write("Files from the directory are:\n\n")
    fobj.write(Border+"\n")

    for Foldername, subfilename, filename in os.walk(DirectoryPath):
        for fname in filename:
            fobj.write(fname+"\n")
    
    fobj.write(Border+"\n")
    fobj.write("Log file gets created at : "+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()
    print("Log file created successfully.\n")


def main():
    Border = "-" * 40

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):
        
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the scipt as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        
        else:
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
        print(Border)
        print(" Thank you for using Marvellous Automation Script ")
        print(Border)

if __name__ == "__main__":
    main()