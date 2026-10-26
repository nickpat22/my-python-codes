###############################################################
#
# Importing Required Libraries
#
################################################################

import psutil
import sys
import os
import time
import schedule
import smtplib
import mimetypes
from email.message import EmailMessage

###############################################################
#
#Function naame : Directorycanner
#Input: Name of Directory
#Description: Deletes all empty files periodically
#Date: 19/07/2026
#Author: Nikunj Mahendra Patidar
#
################################################################

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

def send_mail(sender,app_password,receiver,subject,body,attachment_path =None):
    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set mail headers
    msg["From"] = sender
    msg["To"] =receiver
    msg["Subject"] =subject

    # Step 3 : Add mail body
    msg.set_content(body)
    # Attach file if provided
    if attachment_path:
        with open(attachment_path, "rb") as file:
            file_data = file.read()

        mime_type, _ = mimetypes.guess_type(attachment_path)

        if mime_type is None:
            mime_type = "application/octet-stream"

        maintype, subtype = mime_type.split("/", 1)

        msg.add_attachment(
            file_data,
            maintype=maintype,
            subtype=subtype,
            filename=os.path.basename(attachment_path)
        )
        # Step 4 : Create SMTP SSL connection manually
        # Step 5 : Login using Gmail + App password
        # Step 6 : Send the email
        # Step 7 : Close connection manually
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)
DeletedFiles = []
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

        for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
            for fname in FileName:
                TotalFiles = 0
                TotalFiles = TotalFiles + 1
                fname = os.path.join(FolderName,fname)
                fobj.write(f"{fname} : {os.path.getsize(fname)} bytes\n")
                DeletedFiles.append(fname)


                if(os.path.getsize(fname)==0):
                    EmptyFiles = 0
                    EmptyFiles = EmptyFiles + 1
                    os.remove(fname)
                SendMailDelete()


        fobj.write("\n" + Border + "\n")
        fobj.write(f"Total Files Scanned : {TotalFiles}\n")
        fobj.write(f"Total empty Files Found and deleted {EmptyFiles}\n")
        
        fobj.write(Border+"\n")
        fobj.write("Log File Gets Created At : " + timestamp + "\n")
        fobj.write("\n"+Border+"\n")
        fobj.close()

    print("Log file created successfully.\n")

def SendMailDelete():
    # Always use separate temporary/testing account
    sender_email ="nikunjpatidar9271712740.1302@gmail.com"

    # App password generated from Google account
    app_password ="ldea axwz srre gimg"

    # Your second email for testing
    receiver_email ="pruthvirajpawar964@gmail.com"
    timestamp = time.ctime()
    subject = (f"File Delated At Time {timestamp} ")

    body = """Jay Ganesh,
    This is a test email sent using Marvellous Python.
    Regards,
    Marvellous Infosystems"""
    fname =DeletedFiles[0]
    attachment = fname   # Change this path

    send_mail(sender_email, app_password, receiver_email, subject, body)

    print("Marvellous Mail Sent Successfully")

def SendMailUsage():
    # Always use separate temporary/testing account
    sender_email ="nikunjpatidar9271712740.1302@gmail.com"

    # App password generated from Google account
    app_password ="ldea axwz srre gimg"

    # Your second email for testing
    receiver_email ="pruthvirajpawar964@gmail.com"
    timestamp = time.ctime()
    subject = (f" Memory Usage at {timestamp} ")

    body = """Jay Ganesh,
    This is a test email sent using Marvellous Python.
    Regards,
    Marvellous Infosystems"""

    attachment = r"C:\Users\Nikunj\Desktop\DeleteLog.txt"   # Change this path

    send_mail(sender_email, app_password, receiver_email, subject, body)

    print("Marvellous Mail Sent Successfully")
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
    Border = "-"*60
    print(Border)
    print("----- Marvellous Platform Survelence System -----")
    print(Border)
    
        # --h & --u Handelling
    if(len(sys.argv)==2):
        if (sys.argv[1]) == "--h" or sys.argv[1] == "--H":
            print("\n--------------------Platform Survillence--------------------\n")
            print("This automation script is used to perform")
            print("It fetches info about running process")
            print("it fetch info about Primary storage as Ram")
            print("it fetch info about secondary storage as hdd")
            print("it fetch info about Microprocessor")
            print("It gets autoschedule periodically")
            print("It maintains all records into log file")
            print("It sends the log file through mail periodically")
            print("\n--------------------Disk Sanitizer--------------------\n")
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
            print("\n-------------------------------------------------------\n")
        elif(sys.argv[1]) == "--u" or sys.argv[1] == "--U":
            print("\n--------------------Platform Survillence--------------------\n")
            print("Use the automation Script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in Minuts in periodic execution")
            print("Folder_Name : Name of folder for the log file creation")
            print("\n--------------------Disk Sanitizer--------------------\n")
            print("Please execute the scipt as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
            print("\n-------------------------------------------------------\n")
        else:
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)
            
    
    
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
###############################################################
#
#Starter of the Automation Script
#
################################################################

if __name__ == "__main__":
    main()


