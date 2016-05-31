import __future__
from sort_helper import less, exchange, test_sort

def my_sort(array):

    if len(array) < 10:
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

    mid = len(array)//2
    left = my_sort(array[:mid])
    right = my_sort(array[mid:])

    if left[-1] <= right[0]:
        left.extend(right)
        return left

    
    

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        elif left[i] > right[j]:
            array[k] = right[j]
            j+=1
        k+=1

    while i < len(left):
        array[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        array[k] = right[j]
        k += 1
        j += 1
    return array


if __name__ == "__main__":
    test_sort(my_sort,size =25, toPrint = True )





