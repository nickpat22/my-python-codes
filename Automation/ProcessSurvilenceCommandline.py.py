#python ProcessSurvilence.py 2 Marvellous
#python ProcessSurvilence.py File_interval  Folder_Name
#           0                       1           2
# 
import psutil
import sys
import os


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
    elif(sys.argv[3]):
        pass



    print(Border)
    print("Thank You For using our Automation System")
    print(Border)

    
if __name__ =="__main__":
    main()