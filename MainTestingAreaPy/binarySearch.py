# Iterative Binary Search Function
# It returns location of x in given array arr if present,
# else returns -1
import math as m


def binarySearch(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:

        mid = m.ceil((l + r) / 2)

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right halfh
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, x)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
