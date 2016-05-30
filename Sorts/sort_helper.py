import __future__
import random

def exchange(l, i, j):
    """ Exchanges items i and j in list L
    """
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def less(i, j, func = None):
    if not func:
        return i < j
    else:
        return func(i) < func(j)

def is_sorted(l):
    """ Determines if the list is sorted.
    """
    for i in xrange(len(l)-1):
        if less(l[i+1], l[i]):
            return False

    return True

def test_sort(sort_function, size = 10):
    test = [i for i in xrange(size)]
    random.shuffle(test)
    print(test)
    test= sort_function(test)
    print(test)
    assert(is_sorted(test))

if __name__ == "__main__":
    ls = [1,2,3]

    print(is_sorted(ls))

    exchange(ls,0, 2)
    print(is_sorted(ls))
    print([i for i in xrange(10)])

