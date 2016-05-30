# Sort Algorithms

## sort_helper.py
helper functions to make implementation easier. Includes exchange(), less(), is_sorted(), and test()

## selection_sort.py
Find the smallest item in the array, and exchange it with the first. Find the next smallest item, exchange with the 2nd, etc.
### Analysis
*  O(N^2)
*  running time is insensitive to input. Arrangement of input does not affect running time (Only size of input)
*  Minimal data movement. N exchanges.
*  N = 1000, run 10 times, t = 0.734

## insertion_sort.py
scans through array. All values to the left of i are sorted. i is inserted in sorted order on the left side, larger values are shifted to the right one.

### Analysis
*  Average N^2
*  Best case: N
*  Very fast for partially sorted or small arrays
*  Can be fast on even large arrays if partially sorted
*  N = 1000, run 10 times, t = 0.004
*  N = 10000, run 3 times, t = 4.47s

## Shell Sort
Similar to insertion sort, except sorts intervals of the original array as if they were independent lists. Uses interval sequence of ((3\*\*k)-1)/2) no greater than N//3

### Analysis
*  Much faster than insertion sort on large arrays
*  Essentially insertion sort at N < 12, with additional overhead.
*  Worst case N^(3/2)
*  Can be thought of as insertion short of h intervals of the array, treated as sub lists.
*  N = 1000, run 10 times, t = 0.017
*  N = 10000, run 3 times, t = 0.08s
*  N = 100000, run 3 times, t = 1.70s
*  N = 1000000, run 3 times, t = 25s

