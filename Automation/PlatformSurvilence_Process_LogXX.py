import psutil
import sys
import os
import time
import schedule

def ProcessScan():
    listprocess = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()
        listprocess.append(info)

    return listprocess

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
    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Platform Survelence System -----\n")
    fobj.write("Log File Gets Created at : "+timeStamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-----------System Report----------------\n")

    #CPU Information
    fobj.write("No of active CPU Core : %s \n"%psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n"%psutil.cpu_percent())
    fobj.write(Border+"\n")

    #RAM INFORMATION
    memory = psutil.virtual_memory()

    fobj.write("RAM Usage : %s %%\n"%memory.percent)
    fobj.write("Total RAM Available : %s\n"%memory.total)
    
    fobj.write(Border+"\n")

    #Network Usage 
    netobj = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))

    #Process Log
    Data = ProcessScan()

    for info in Data:
        #fobj.write(f"{info}\n")
        fobj.write("PID : %s \n" %info.get("pid"))
        fobj.write("Name : %s \n" %info.get("name"))
        fobj.write("User Name : %s \n" %info.get("username"))
        fobj.write("Status : %s \n" %info.get("status"))
        fobj.write("CPU Usage : %.2f \n" %info.get("cpu_percent"))
        fobj.write("RAM usage : %.2f \n" %info.get("memory_percent"))
        fobj.write(Border+"\n")


    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write("-----------End of Log File-------------\n")
    fobj.write(Border+"\n")

    fobj.close()



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

        #print("CPU Usage : ",psutil.cpu_percent())
        print("Schedular Started Sucessfully")
        print("Press Ctrl + C to abort automation Script")
        
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