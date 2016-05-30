import __future__
from sort_helper import less, exchange, test_sort

def my_sort(array):

    for i in xrange(1, len(array)):
        value = array[i]
        shift_made = False
        empty_position = None
        for j in reversed(xrange(1,i+1)):
            if less(value, array[j-1]):
                #  Shift larger values to the right instead of doing full exchanges. Cuts array access in half.
                array[j] = array[j-1]
                shift_made = True
                empty_position = j-1
            else:
                break
        #  insert original value into position
        if shift_made:
            array[empty_position] = value
                

    return array
test_sort(my_sort, )
            









