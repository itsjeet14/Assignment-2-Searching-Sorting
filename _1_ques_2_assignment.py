"""Implement Binary Search"""

def binary_search(arr, left, right, x):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, right, x)
    else:
        return -1

# get user input for the array and the element to search for
arr = list(map(int, input("Enter the sorted array: ").split()))
x = int(input("Enter the element to search for: "))

# perform binary search on the array
result = binary_search(arr, 0, len(arr) - 1, x)

# print the result of the binary search
if result != -1:
    print("Element", x, "is present at index", result)
else:
    print("Element", x, "is not present in the array")
