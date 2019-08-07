def find_pivot(input_list,low, high):
    
        
    # base cases
    if high < low : 
        return -1
    if high == low:
        return low 
    mid = low + (high-low) // 2
    if ( mid < high and input_list[mid] > input_list[mid+1]) :
        return mid
    if ( mid > low and input_list[mid-1] > input_list[mid]):
        return mid - 1 
    if (input_list[low] >= input_list[mid]):
        return find_pivot(input_list, low,mid-1)

    return find_pivot(input_list, mid+1, high)
    
    
def binary_search(input_list, low, high, number):
    if low > high:
        return -1
    mid = low + (high-low) // 2
    if (input_list[mid] == number):
        return mid
    if ( number > input_list[mid]):
        return binary_search(input_list, mid+1, high, number)
    return binary_search(input_list, low, mid-1, number)
    
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
       
    Idea is to find pivot element in the array, divide the array based on pivot point into two sub arrays and do binary search
    for a sorted array, pivot is the element for which the one next to it is smaller than it. this takes O(logn) time.
    
    Input arr[] = {3, 4, 5, 1, 2}
    Element to Search = 1
      1) Find out pivot point and divide the array in two
          sub-arrays. (pivot = 2) /*Index of 5*/
      2) Now call binary search for one of the two sub-arrays.
          (a) If element is greater than 0th element then
                 search in left array
          (b) Else Search in right array
              (1 will go in else as 1 < 0th element(3))
      3) If element is found in selected sub-array then return index
     Else return -1.
    """
    low = 0
    high = len(input_list) - 1
    pivot =find_pivot(input_list,low, high)
    
    # if no pivot, then array is not rotated at all
    if pivot == -1:
        return binarySearch(input_list, low, high, number)
    #If we found a pivot, then first compare with pivot 
    #and then search in two subarrays around pivot
    if (input_list[pivot] == number) :
        return pivot
    if (input_list[low] <= number):
        return binary_search(input_list, low, pivot-1, number)
    return binary_search(input_list, pivot+1, high, number)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
 
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


print(rotated_array_search([5,6,7,8,9,10, 1,2,3],3)) #prints 8
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)) #prints 0
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)) # prints5
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8)) # prints 2
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1)) #prints 3
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10)) # prints -1
print(rotated_array_search([6, 7, 8, 9, 10, 11, 12], 10)) # prints 4

test_function([[5,6,7,8,9,10, 1,2,3],3])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 11, 12], 10])