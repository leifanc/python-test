import threading
import time


def loop():
    print "Thread %s is running" % threading.current_thread().name
    for i in range(5):
        print '%s >> %s' % (threading.current_thread().name, i)
        time.sleep(1)
    print 'Thread %s ended' % threading.current_thread().name


print "Thread %s is running" % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name




