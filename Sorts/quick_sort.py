import __future__
import random
import insertion_sort
from sort_helper import less, exchange, test_sort

def my_sort(array):
    #random.shuffle(array)

    quicksort(array)
    return insertion_sort.my_sort(array)

def quicksort(array, begin=0, end= None):
    if end is None:
        end = len(array)-1

    if begin + 10 > end:
        return

    pivot = partition(array, begin, end)
    quicksort(array, 0, pivot -1)
    quicksort(array, pivot+1, end)
    
def partition(array, begin, end):
    m = median_of_three(array, begin, end)
    p = begin
    for i in xrange(begin, end +1):
        if i == m:
            continue
        if array[i] <= array[begin]:
            p +=1
            array[i], array[p] = array[p], array[i]
    array[m], array[p] = array[p], array[m]
    return p

def median_of_three(array, begin, end):
    m = [array[begin], array[begin+(end-begin)//2], array[end]]
    m.remove(min(m))
    m.remove(max(m))
    return m[0]

if __name__ == "__main__":
    test_sort(my_sort,size = 500, toPrint = False )

