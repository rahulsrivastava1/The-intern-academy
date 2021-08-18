# Desktop notifier

# importing modules
from plyer import notification
import time

#declaring function
def notifyMe(title,msg):
    notification.notify(
        title=title,
        message=msg,
        timeout=5
    )

# driver code
if __name__=="__main__":
    notifyMe("React developing time!","Rahul,learn React JS!")
    time.sleep(10)
    notifyMe("Internship projects time!","Do internship projects")
    time.sleep(10)
    notifyMe("DSA using C++","Practice DSA programs using gfg")
    time.sleep(5)
    print("Done!")