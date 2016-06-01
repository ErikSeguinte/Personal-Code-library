import __future__
import random
import insertion_sort
from sort_helper import less, exchange, test_sort

def my_sort(array):
    #random.shuffle(array)

    quicksort(array)
    return array

def quicksort(array, begin=0, end= None):
    if end is None:
        end = len(array)-1

    if end <= begin + 10:
        array[begin:end+1] =insertion_sort.my_sort(array[begin:end+1])
        return


    pivot = partition(array, begin, end)
    if pivot <= (begin+end)//2:
        quicksort(array, 0, pivot -1)
        quicksort(array, pivot+1, end)
    else:
        quicksort(array, pivot+1, end)
        quicksort(array, 0, pivot -1)
    
def partition(array, begin, end):
    m = median_of_three(array, begin, end)
    array[begin], array[m] = array[m], array[begin]
    array[begin]
    value = array[begin]
    i = begin+1
    j = end


    while True:
        while array[i] < value:
            i += 1
            if i >= end:
                break
        while array[j] > value:
            j -= 1
            if j<= begin+1:
                break
        if i >= j:
            break
        array[i], array[j] = array[j], array[i]

    array[begin], array[j] = array[j], array[begin]
    return j


        

def median_of_three(array, begin, end):
    mid = (begin + end) //2
    m = [array[begin], array[mid], array[end]]
    if m[0] < m[1]:
        return mid if m[1] > m[2] else end
    else:
        return begin if m[0] < m[2] else end

if __name__ == "__main__":
    test_sort(my_sort, toPrint = True, size= 10000 )

