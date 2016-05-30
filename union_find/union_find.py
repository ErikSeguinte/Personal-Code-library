import __future__

class UF(object):

    def __init__(self, size):
        self.uf = list()
        self.count = size
        self.sizes = [0]*size
        for i in xrange(size):
            self.uf.append(i)

    def union(self, p, q):
        """ Connect 2 nodes
        """

        # No need to connect if already connected
        if self.connected(p,q):
            return

        pRoot = self.find(p)
        qRoot = self.find(q)
        self.count -= 1

        if self.sizes[qRoot] < self.sizes[pRoot]:
            self.uf[qRoot] = pRoot
            self.sizes[pRoot] += self.sizes[qRoot]
        else:
            self.uf[pRoot] = qRoot
            self.sizes[qRoot] += self.sizes[pRoot]

    def find(self, p):
        """ Return representation of node.

        Recursive implementation, also applies path compression.
        """

        if p == self.uf[p]:
            return p

        pRoot = self.find(self.uf[p])
        
        # Path Compression.
        self.uf[p] = pRoot        

        return pRoot


    def connected(self, p, q):
        """ Determines if p and q are connected.
        """
        return self.find(q) == self.find(p)


    def count(self):
        """ Counts the number of components.

        Number of components starts at N, decrements everytime there is a new merge.
        """
        pass
    
if __name__ == "__main__":
    uf = UF(10)
    uf.union(4, 3)
    uf.union(3, 8)
    uf.union(6, 5)
    uf.union(9, 4)
    uf.union(2, 1)
    uf.union(8, 9)
    uf.union(5, 0)
    uf.union(7, 2)
    uf.union(6, 1)
    uf.union(1, 0)
    uf.union(6, 7)
    print(uf.connected(0,5))
    print(uf.connected(3,4))
    print(uf.connected(0,9))
    print(uf.connected(4,1))

