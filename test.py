import json
try:
    import cPickle as pickle
except ImportError:
    import pickle

with open('d:/IO_test/test', 'w') as w:
    w.write('HELLO')
with open('d:/IO_test/test', 'r') as r:
    print r.read()

d = dict(name ='job', age=20)
with open('d:/IO_test/test', 'w') as f:
    pickle.dump(d, f)
with open('d:/IO_test/test', 'r') as f:
    print pickle.load(f)

print json.dumps(d)
with open('d:/IO_test/test', 'w') as f:
    json.dump(d,f)