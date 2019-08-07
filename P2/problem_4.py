def swap(input_list, i, j):
    temp = input_list[i]
    input_list[i] = input_list[j]
    input_list[j] = temp
def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start = 0
    mid = 0
    pivot = 1
    end = len(input_list)-1
    while mid <= end :
        if input_list[mid] < pivot: # current element less than 1
            swap(input_list, start,mid)
            start += 1
            mid += 1
        elif input_list[mid] > pivot: #current element is 2
            swap(input_list,mid, end)
            end -= 1
        else:
            mid += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    #print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([])
test_function([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])