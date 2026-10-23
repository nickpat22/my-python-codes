import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryPath="Marvellous"):
    timestamp = time.ctime()
    LogFileName = (f"Marvellous{timestamp}.log")
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = False
    Ret = os.path.exists(DirectoryPath)

    if (Ret == False):
        print("Automation Error : There is No such Directory with Name ",DirectoryPath)
        return
    
    Ret = os.path.isdir(DirectoryPath)
    if (Ret == False):
        print("Automation Error : There is no Directory with Name",DirectoryPath)
        return
    
    print("Log File Gets Created With Name :", LogFileName)


    fobj = open(LogFileName,"w")
    Border = "-"*40
    fobj.write(Border + "\n\n")
    fobj.write("Marvellous Automation Script\n")
    fobj.write("Files From The Directory Are :\n")
    fobj.write(Border + "\n\n")

    TotalFiles = 0
    EmptyFiles = 0

    for Foldername, SubFolder, Filename in os.walk(DirectoryPath):
        for fname in Filename:
            TotalFiles = TotalFiles + 1
            fname = os.path.join(Foldername,fname)
            fobj.write(f"{fname} : {os.path.getsize(fname)} bytes\n")

            if (os.path.getsize(fname)==0):
                EmptyFiles = EmptyFiles + 1
                os.remove(fname)
    fobj.write("\n"+Border+"\n")
    fobj.write(f" Total number of file Scanned : {TotalFiles}\n")
    fobj.write(f"Total number of empty files : {EmptyFiles}\n")
    fobj.write("\n"+Border+"\n")
    fobj.write(f"The File is Created at :{timestamp}\n")
    fobj.write("\n"+Border+"\n")
    fobj.close()

    print("Log file created successfully.\n")


def main():
    Border = "-"*40
    print(Border)
    print("Welcome to Automation")

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("Help")
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Usage")
        else:
           DirectoryName = sys.argv[1]
           schedule.every(1).minute.do(DirectoryScanner,DirectoryName)
           while True:
               schedule.run_pending()
               time.sleep(1)

    else:
        print("Invalid Command")
        print("Try using --h or --u")

if __name__ == "__main__":
    main()