def get_min_max_recursive(ints, low, high):
    if low == high:
        max = ints[low]
        min = ints[low]
        
        return min, max
    if high == low + 1:
        if ints[low] > ints[high]:
            max = ints[low]
            min = ints[high]
        else:
            max = ints[high]
            min = ints[low]
        return min, max
    mid = (low + high) // 2
    minl, maxl = get_min_max_recursive(ints, low, mid)
    minr, maxr = get_min_max_recursive(ints,mid+1, high)
     
    if minl < minr:
        min = minl
    else:
        min = minr
     
    if maxl > maxr:
        max = maxl
    else:
        max = maxr
    return min,max
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    low = 0
    high = len(ints)-1
    min, max = get_min_max_recursive(ints, low, high)
    return min, max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print(get_min_max([5]))  # (5, 5)
print(get_min_max([10, 5, 6, 0, 12, 8]))  # (0, 12)
print(get_min_max([5, 7, 17, 23, 11]))  # (5, 23)
print(get_min_max([1, 27, 27, 5, 6, 0, 12, 8, 9, 4, 4, 2, 20]))  # (0, 27)