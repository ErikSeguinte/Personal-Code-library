import __future__
import timeit, random
import insertion_sort, selection_sort, shell_sort, quick_sort2
import merge_sort, heap_sort
import sort_helper


sorts = [
        # selection_sort.selection_sort,
        #  insertion_sort.my_sort,
        shell_sort.my_sort,
        merge_sort.my_sort,
        quick_sort2.my_sort,
        heap_sort.my_sort
        ]
            

def time_sort():
    N = 10000
    array = [x for x in xrange(N)]
    random.shuffle(array)
    def wrap_sort(my_sort, array):
        
        def wrapped():
            my_sort(list(array))
        return wrapped

    for my_sort in sorts:
        print(my_sort.func_name)
        wrapped = wrap_sort(my_sort, array)
        print(timeit.timeit(wrapped, number = 100))
        print(timeit.timeit(wrapped, number = 100))
        print(timeit.timeit(wrapped, number = 100))



#  def time_class():
#      N = 10000000
#      array = [x for x in xrange(N)]
#      random.shuffle(array)
#      def wrap_sort(my_sort, array):
#          
#          def wrapped():
#              sort_helper.test_class(my_sort, seq=array, toPrint=False)
#          return wrapped
#  
#      for my_sort in classes:
#          wrapped = wrap_sort(my_sort, array)
#          print(timeit.timeit(wrapped, number = 2))

time_sort()
