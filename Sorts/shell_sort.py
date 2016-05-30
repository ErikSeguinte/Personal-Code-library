import __future__
from sort_helper import less, exchange, test_sort
from collections import deque

def my_sort(array):

    def interval_sequence():
        N = len(array)
        seq = deque()
        k = 1
        while True:
            value = ((3**k)-1)//2
            if value > N//3:
                break
            seq.appendleft(value)
            k += 1

        
        return seq 
    for h in interval_sequence():

        for i in xrange(h, len(array)):
            value = array[i]
            shift_made = False
            empty_position = None
            for j in xrange(i, h-1, -h): 
                if less(value, array[j-h]) and j >= h:
                    #  Shift larger values to the right instead of doing full exchanges. Cuts array access in half.
                    array[j] = array[j-h]
                    shift_made = True
                    empty_position = j-h
                else:
                    break
            #  insert original value into position
            if shift_made:
                array[empty_position] = value
                

    return array

if __name__ == "__main__":
    test_sort(my_sort, size = 10000, toPrint = False) 



