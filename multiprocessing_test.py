from multiprocessing import Process
import os

def run_child(name):
    print 'i am child process %s(%s)' %(name, os.getpid())

if __name__ == '__main__':
    p = Process(target = run_child, args = ('test',))
    p.start()
    p.join()
    print 'all end'
