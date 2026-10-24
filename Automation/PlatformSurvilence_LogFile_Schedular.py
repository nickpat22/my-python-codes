import psutil
import sys
import os
import time
import schedule

def PlatformSurvelienve(FolderName):
    Border = "-"*50

    Ret = False
    Ret = os.path.exists(FolderName)

    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable To Procced as Directory name is exesting but its not a directory")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory For the LogFile Gets Created Sucessfully")

    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timeStamp)

    fobj = open(FileName, "w")

    print(f"Log File Gets Successfully creates with name : {FileName}")

def main():
    Border = "-"*50
    print(Border)
    print("----- Marvellous Platform Survelence System -----")
    print(Border)

    # --h & --u Handelling
    if(len(sys.argv)==2):
        if (sys.argv[1]) == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to perform")
            print("It fetches info about running process")
            print("it fetch info about Primary storage as Ram")
            print("it fetch info about secondary storage as hdd")
            print("it fetch info about Microprocessor")
            print("It gets autoschedule periodically")
            print("It maintains all records into log file")
            print("It sends the log file through mail periodically")

        elif(sys.argv[1]) == "--u" or sys.argv[1] == "--U":
            print("Use the automation Script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in Minuts in periodic execution")
            print("Folder_Name : Name of folder for the log file creation")
            
        else:
            print("Unable to prosside as argument are not matching")
            print("Please use --h or --u flage for getting more deatils")
        


    #Actual Project Code
    elif (len(sys.argv) == 3):
        #PlatformSurvelienve(sys.argv[2])
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvelienve, sys.argv[2])
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid no of argument")
        print("Unable to prossed as argument are not matching")
        print("Please use --h or --u flage for getting more deatils")

    print(Border)
    print("Thank You For using our Automation System")
    print(Border)

    
if __name__ =="__main__":
    main()