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

    print("Log File Gets Created With Name :",LogFileName)
    fobj = open(LogFileName, "w")

    fobj.write("Marvellous Automation Script\n")
    fobj.write("Files From The Directory Are:\n")

    for FolderName, SubFolder, FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fobj.write(fname + "\n")

    fobj.close()          # Corrected


def main():
    Border = "-" * 40
    print(Border)
    print(" Marvellous Automation Script ")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to traverse the directory.")
            print("For better usage please check --u flag")
            return

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Please execute the script as:")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be an absolute path.")
            return

        else:
            DirectoryName = sys.argv[1]      # Corrected

            if os.path.exists(DirectoryName):

                schedule.every(1).minutes.do(DirectoryScanner, DirectoryName)

                print("Scheduler Started...")
                print("Press Ctrl + C to stop.")

                while True:
                    schedule.run_pending()   # Corrected
                    time.sleep(1)

            else:
                print("Directory does not exist.")

    else:
        print("Invalid number of arguments")
        print("Usage: python FileName.py DirectoryName")

    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)


if __name__ == "__main__":
    main()