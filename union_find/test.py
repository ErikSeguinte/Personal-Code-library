import __future__
import union_find
import random

uf = None
size = 0

with open('largeUF.txt', 'r') as inputFile:
    size =(int(inputFile.readline())) 
    uf = union_find.UF(size)
    
    for line in inputFile:
        p, q = line.split(' ')
        uf.union(int(p),int(q))


for i in xrange(1000000):
    p =random.randint(0, size-1)
    q = random.randint(0, size-1)
    connected = uf.connected(p,q)
    if not connected:
        print(uf.connected(p,q))
