import __future__
import sort_helper


def selection_sort(array):

    for i in xrange(len(array)):
        min_value = array[i]
        min_position = None

        for j in xrange(i+1, len(array)):
            if sort_helper.less(array[j], min_value):
                min_value = array[j]
                min_position = j
        if min_position:
            sort_helper.exchange(array, i, min_position)

    return array
sort_helper.test_sort(selection_sort, 3)
            









