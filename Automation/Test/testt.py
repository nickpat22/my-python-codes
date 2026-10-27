import sys
import os
import time
import schedule
import psutil

def ProcessScan():

    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["memory_percent"] = proc.memory_percent(None)
        info["cpu_percent"] = proc.cpu_percent()

        listprocess.append()
    return listprocess
def DisplayProcess(Pname):
    Data = ProcessScan()

    for info in Data:
        if info.get("name") == Pname:
            print("Process Name :%s"%info.get("name"))
            print("Process ID :%s"%info.get("pid"))
            print("Process usnername :%s"%info.get("username"))
            print("Process Status :%s"%info.get("status"))
            print("Memory Percent :%2f"%info.get("cpu_percent"))
            print("Memory Memory :%2f"%info.get("cpu_memory"))
        else:
            print("Error")
        

def main():
    Border = "-"*60
    print(Border)
    print("----------Welcome to Automation Script---------")
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--H" or sys.argv[1] == "--h"):
            print("Help")
        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage")
        else:
            Pname = sys.argv[1]
            DisplayProcess(Pname)
    else:
        print("Invalid Syntax")
        print("Use --h or --u")

if __name__ =="__main__":
    main()