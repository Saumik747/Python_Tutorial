#write a python program to demonstrate three technique to implement multithreading
import time
from threading import Thread
def myfunc(i):
    print("Sleeping 5 sec from thread %d\n" %i)
    time.sleep(5)
    print("Finished sleeping from thread %d\n" %i)
print("Thread without using a Class")
for i in range(10):
    t=Thread(target=myfunc,args=(i,))
    t.start()
print("1 method multithreading is completed")

class MyThread(Thread):
    def run(self):
        for i in range(1,6):
            print("\n Thread %i going to sleep for 5 second." %i)
            time.sleep(5)
            print("\n Thread %i is awake now" %i)
t1=MyThread()
print("Creating thread using subclass")
t1.start()
t1.join()
print("2 method multithreading is completed")

class MyThread1:
    def sleep(self):
        for i in range(1,6):
            print("Thread %i going to sleep for 5 seconds." %i)
            time.sleep(5)
            print("Thread %i is awake now" %i)
obj=MyThread()
t1=MyThread(target=obj.sleep())
print("Creating thread without using subclass")
t1.start()
print("3 method multithreading is complete")
