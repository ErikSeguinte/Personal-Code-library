import __future__

class Heap(object):

    def __init__(self, initial = None, key = None, ):
        self.data = [None]
        self.key = key
        if initial:
            self.data.extend(initial)
            self.orderHeap()


    def orderHeap(self, N = None):
        #  Restore heap order on random ordering. Can start half way back, as we can skip sub-heaps of size 1.

        if not N:
            N = len(self.data) -1
        N = N//2
        for k in xrange(N, 0, -1):
            self.sink(k)


    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def less(self, i, j):
        if self.key:
            return key(self.data[i]) < key(self.data[j])
        else:
            return self.data[i] < self.data[j]

    def swim(self, k):
        """ Restore heap order by swimming up when k is larger than its parent
        """
        
        while self.less(k//2, k) and k > 1:
            self.swap(k, k//2)
            k = k//2

    def sink(self, k, N=None):
        """ Restore heap order by sinking down when k is smaller than one of it's children
        """

        if not N:
            N = len(self.data) - 1
        while (2*k) <= N:
            
            # get left child
            j = k*2


            # Get right child if larger
            if j < N and self.less(j, j + 1):
                j += 1

            if not self.less(k, j):
                #  K larger than J, stop sink.
                break

            self.swap(k, j)

            k = j

    def insert(self, value):

        self.data.append(value)

        self.swim(len(self.data) -1 )

    def printheap(self):
        print(self.data[1:])

    def popMax(self):

        temp = self.data[1]
        self.data[1] = self.data.pop()
        self.sink(1)
        return temp


