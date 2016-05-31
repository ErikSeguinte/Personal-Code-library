import __future__
from sort_helper import less, exchange, test_sort, test_class


class merge_sort(object):

    def __init__(self, array = None):
        self.array = array
        self.aux = [0] * len(array)

    def merge(self, low, mid, high):
        
        left = low
        right = mid + 1
        
        for i in xrange(low, high + 1 ):
            self.aux[i] = self.array[i]

        for i in xrange(low, high + 1 ):
            #  left is empty
            if left > mid:
                self.array[i] = self.aux[right]
                right +=1
            #  right is empty
            elif right > high:
                self.array[i] = self.aux[left]
                left += 1
            # left pointer is higher right pointer
            elif self.aux[left] > self.aux[right]:
                self.array[i] = self.aux[right]
                right += 1
            # right pointer is higher than left pointer
            else:
                self.array[i] = self.aux[left]
                left += 1


    def insertion_sort(self, low, high):

        for i in xrange(low, high + 1):
            value = self.array[i]
            shift_made = False
            empty_position = None
            for j in reversed(xrange(1,i+1)):
                if less(value, self.array[j-1]):
                    #  Shift larger values to the right instead of doing full exchanges. Cuts array access in half.
                    self.array[j] = self.array[j-1]
                    shift_made = True
                    empty_position = j-1
                else:
                    break
            #  insert original value into position
            if shift_made:
                self.array[empty_position] = value
                    

    def m_sort(self, low=0, high= None):
        # base case. Pointers overlap. Nothing to sort.
        if high is None:
            high = len(self.array) - 1
        if high - low < 15:
            self.insertion_sort(low, high)
            return
        if high <= low:
            return

        mid = (high + low)//2
        self.m_sort(low, mid)
        self.m_sort(mid + 1, high)
        self.merge (low, mid, high)

    def sort(self):
        self.m_sort()
        return self.array
if __name__ == "__main__":
    test_class(merge_sort, size = 1000000, toPrint = False )

