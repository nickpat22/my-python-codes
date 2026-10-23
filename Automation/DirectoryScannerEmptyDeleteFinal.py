###############################################################
#
# Importing Required Libraries
#
################################################################

import sys
import os
import time
import schedule

###############################################################
#
#Function naame : Directorycanner
#Input: Name of Directory
#Description: Deletes all empty files periodically
#Date: 19/07/2026
#Author: Nikunj Mahendra Patidar
#
################################################################



def DirectoryScanner(DirectoryPath="Marvellous"):
    Border = "_" * 40
    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log" % (timestamp)
    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    Ret = False
    Ret = os.path.exists(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : There is No such Directory with Name",DirectoryPath)
        return
    
    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation Error : It is not a Directory with name",DirectoryPath)
        return
    

    print("Log File Gets Created With Name :", LogFileName)

    with open(LogFileName, "w") as fobj:

        fobj.write(Border + "\n\n")
        fobj.write("Marvellous Automation Script\n")
        fobj.write("Files From The Directory Are :\n")
        fobj.write(Border + "\n\n")

        TotalFiles = 0
        EmptyFiles = 0

        for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
            for fname in FileName:
                TotalFiles = TotalFiles + 1
                fname = os.path.join(FolderName,fname)
                fobj.write(f"{fname} : {os.path.getsize(fname)} bytes\n")


                if(os.path.getsize(fname)==0):
                    EmptyFiles = EmptyFiles + 1
                    os.remove(fname)


        fobj.write("\n" + Border + "\n")
        fobj.write(f"Total Files Scanned : {TotalFiles}\n")
        fobj.write(f"Total empty Files Found and deleted {EmptyFiles}\n")
        
        fobj.write(Border+"\n")
        fobj.write("Log File Gets Created At : " + timestamp + "\n")
        fobj.write("\n"+Border+"\n")
        fobj.close()

    print("Log file created successfully.\n")
###############################################################
#
#Function naame : Main
#Input:           CommandLine Arguments
#Description:     It Controles The Script
#Date: 19/07/2026
#Author: Nikunj Mahendra Patidar
#
################################################################

def main():
    Border = "-" * 40

    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if len(sys.argv) == 2:

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
###############################################################
#
#Starter of the Automation Script
#
################################################################

if __name__ == "__main__":
    main()