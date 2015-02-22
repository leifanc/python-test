from multiprocessing import Pool
import os
import time
import random


def run_child(name):
    print 'i am child process %s(%s)' % (name, os.getpid())
    time.sleep(random.random() * 3)
p = Pool()
for i in range(4):
    p.apply_async(run_child, args=(i,))
p.close()
p.join()
print 'all end'
