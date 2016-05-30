import __future__
import timeit, random
import insertion_sort, selection_sort, shell_sort


sorts = [insertion_sort.my_sort, shell_sort.my_sort]

def time_sort():
    N = 100
    array = [x for x in xrange(1000)]
    random.shuffle(array)
    def wrap_sort(my_sort, array):
        
        def wrapped():
            my_sort(array)
        return wrapped

    for my_sort in sorts:
        wrapped = wrap_sort(my_sort, array)
        print(timeit.timeit(wrapped, number = 100))


time_sort()
