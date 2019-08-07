def countSort(arr):
    min = 0
    max = 9
    count = []
    z = 0
    k = len(arr)-1
    count = [0 for i in range(10)] 
    n = len(arr)
    for i in range(0,n):
        count[arr[i]] += 1
    for i in range(10):
        while count[i] > 0 :
            arr[k] = i
            k -= 1
            #for ascending order 
            #arr[z] = i 
            #z += 1
            count[i] -= 1
            
    return arr


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    if input_list is None:
        return None
    if len(input_list) <= 1 :
        return input_list
    sorted_list = countSort(input_list)
    first = 0
    for i in range(0,len(sorted_list),2):
        first = first * 10 + sorted_list[i]
    second = 0
    for i in range(1,len(sorted_list),2):
        second = second * 10 + sorted_list[i]
    
    return first, second
    

#input_list = [9,4,1,7,9,1,2,0]

#print(sorted_list)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print(rearrange_digits([4, 6, 2, 5, 9, 8]))  # [964, 852]]

print(rearrange_digits([2, 1]))  # [2, 1]

print(rearrange_digits([42]))  # [42]

print(rearrange_digits(None))  # None

print(rearrange_digits([2, 1, 9, 7, 8]))  # [971, 82]

print(rearrange_digits([8, 7, 6, 4, 2, 1]))  # [862, 741]

print(rearrange_digits([1, 2, 3, 4, 5])) # [531,42]

print(rearrange_digits([4, 6, 2, 5, 9, 8])) # [964, 852]

test_function([[4,6,2,7,9,8],[974,862]])
test_function([[1, 2, 3, 4, 5], [531, 42]])
test_function( [[4, 6, 2, 5, 9, 8], [964, 852]])
