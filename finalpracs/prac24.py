#write a python program to implement race condition
import threading
x=0
COUNT=1000000
def foo():
    global x
    for i in range(COUNT):
        x+=1
def fbar():
    global x
    for i in range(COUNT):
        x=-1
t1=threading.Thread(target=foo)
t2=threading.Thread(target=fbar)
t1.start()
t2.start()
t1.join()
t2.join()
print(x)
