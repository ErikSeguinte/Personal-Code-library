import __future__
import random
import insertion_sort
from sort_helper import less, exchange, test_sort

def my_sort(array):
    random.shuffle(array)

    array= quicksort(array)
    return array

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def quicksort(array, begin=0, end= None):
    if end is None:
        end = len(array)-1

    if end <= begin + 10:
        array[begin:end+1] =insertion_sort.my_sort(array[begin:end+1])
        return array


    pivot = median_of_three(array, begin, end)
    
    left = quicksort([x for x in array if x < pivot])
    middle = [x for x in array if x == pivot]
    right = quicksort([x for x in array if x > pivot])
    return left + middle + right
    
def partition(array, begin, end):
    m = median_of_three(array, begin, end)
    value = array[m]

    

    array[begin], array[j] = array[j], array[begin]
    return j


        

def median_of_three(array, begin, end):
    mid = (begin + end) //2
    a, b, c = array[begin], array[mid], array[end]
    
    if a<=b<=c or c<=b <= a:
        return b
    elif b<=a<=c or c<=a<=b:
        return a
    else:
        return c

if __name__ == "__main__":
    test_sort(my_sort, toPrint = False, size= 250 )

