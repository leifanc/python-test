from multiprocessing import Queue, Process
import time
import random


def write(q):
    for value in ['A', 'B', 'C']:
        print 'put %s to queue' % value
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        value = q.get()
        print 'get %s from queue' % value


q = Queue()
pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))
pw.start()
pr.start()
pw.join()
pr.terminate()