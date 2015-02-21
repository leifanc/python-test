# coding=utf-8
import os

print 'i am parent process： %s' % os.getpid()
pid = os.fork()
if pid == 0:
    print 'i am child process: %s, my father is %s' % (os.getpid(), os.getppid())
else:
    print 'i am parent process： %s' % os.getpid()