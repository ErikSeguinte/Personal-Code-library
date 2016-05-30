# Sort Algorithms

## sort_helper.py
helper functions to make implementation easier. Includes exchange(), less(), is_sorted(), and test()

## selection_sort.py
Find the smallest item in the array, and exchange it with the first. Find the next smallest item, exchange with the 2nd, etc.
### Analysis
*  O(N^2)
*  running time is insensitive to input. Arrangement of input does not affect running time (Only size of input)
*  Minimal data movement. N exchanges.

## insertion_sort.py
scans through array. All values to the left of i are sorted. i is inserted in sorted order on the left side, larger values are shifted to the right one.

### Analysis
*  Average N^2
*  Best case: N
*  Very fast for partially sorted or small arrays
