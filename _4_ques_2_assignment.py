"""Implement Insertion Sor"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# get user input for the array to be sorted
arr = list(map(int, input("Enter the array to be sorted: ").split()))

# perform insertion sort on the array
insertion_sort(arr)

# print the sorted array
print("Sorted array:", arr)
