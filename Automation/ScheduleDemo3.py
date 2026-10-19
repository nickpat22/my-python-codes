import schedule
import time
import datetime

def Display():
    print("Jay Ganesh...",datetime.datetime.now())
def main():
    print("Automation Script Started")

    schedule.every(1).minute.do(Display)
    
    while True:
        schedule.run_pending()
        time.sleep(1)


print("End of Automation Script")
if __name__ == "__main__":
    main()