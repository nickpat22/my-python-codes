import schedule
import time
import datetime

def Display():
    print("Jay Ganesh...",datetime.datetime.now())
def main():
    print("Automation Script Started")

    schedule.every(1).minute.do(Display)
    #issue

if __name__ == "__main__":
    main()