import psutil
import sys
import os
import time
import schedule
Border = "-"*60


def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name", "username","status"])
        info["cpu_percent"] = proc.cpu_percent()
        info["memory_percent"] = proc.memory_percent

        listprocess.append(info)
    return listprocess

def ProcesInfoStore(FolderName):
    Ret = False
    Ret = os.path.exists(FolderName)
    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to proceed as directory name is existing but its nota adirectory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log is created sucessfully")

    timestamp = time.strftime("%y-%m-%d-%H-%M-%S")
    FileName = os.path.join(FolderName,"Nikunj_%s.log"%timestamp)
    fobj = open(FileName,'w')
    print(f"Logfile gets Sucessfully Created with the Name : {FileName}")

    fobj.write("----------------------------------------------\n")
    fobj.write("--------Display Info of running Process-------\n")
    Data = ProcessScan()

    for info in Data:
        fobj.write("Name : %s\n"%info.get("name"))
        fobj.write("PID : %s\n"%info.get("pid"))
        fobj.write("User Name : %s\n"%info.get("username"))
        fobj.write("----------------------------------------------\n")

    fobj.close()

        

def main():
    print(Border)
    print("-----------Welcome to automation Script----------")
    print(Border)
    if len(sys.argv) == 2:
        print("-----------Welcome to ProcessScanning Script----------")
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to perform ")
            print("1 : It fetch the information of running processess")
            print("2 : It fetch information about the primary storage as RAM")
            print("3 : It fetch information about the secondary storage as HDD")
            print("4 : It fetch the information about the microprocessor")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Folder_Name")

        else:
                schedule.every(1).minutes.do(ProcesInfoStore,sys.argv[1])
                while True:
                    schedule.run_pending()
                    time.sleep(1)
                    
            

    else:
        print("Invalid number of argumenst")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("--- Thank you for using our automation System ---")
    print(Border)


if __name__ == "__main__":
    main()