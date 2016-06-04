import __future__
import heap
from sort_helper import less, exchange, test_sort

def my_sort(array):

    h = heap.Heap(array)

    N = len(h.data) -1

    while N > 1:
        h.swap(1, N)
        N -=1
        h.sink(1, N) 
    return h.data[1:]


    return array
if __name__ == "__main__":
    test_sort(my_sort,size = 10, toPrint = True )

