import threading

money = 0
lock = threading.Lock()
def add1(n):
    global money
    money = money + n
    money = money - n


def runThread():
    for n in range(10000):
        lock.acquire()
        try:
            add1(n)
        finally:
            lock.release()


t1 = threading.Thread(target=runThread, name='LockThread1')
t2 = threading.Thread(target=runThread, name='LockThread2')
t1.start()
t2.start()
t1.join()
t2.join()
print money