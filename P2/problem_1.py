def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    if number is None:
        print("No number is given")
        return 0
    if number < 0 :
        print("Negative number")
        return 0
    if(number == 0 or number == 1):
        return number
    # start binary search to find a number between 1 and given number
    start = 1
    end = number
    while start <= end :
        mid = start + (end-start) // 2
        # if x is perfect square
        if (mid * mid == number):
            return mid
        # if mid is smaller than number, 
        #do binary search between mid+1 and end. In this case, we also update ans and take floor value.
        if (mid*mid < number):
            start = mid + 1
            # end remains same as number
            ans = mid
        else:
            # mid*mid is greater than number
            # thus number is smaller
            # so binary search between start and mid
            end = mid - 1
    return ans


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print(sqrt(None))  # return 0
print(sqrt(-7))  # return 0
print(sqrt(0))  # return 0
print(sqrt(1))  # return 1
print(sqrt(4)) # return 2
print(sqrt(9))  # return 3
print(sqrt(16)) # return  4
print(sqrt(27))  # return 5



