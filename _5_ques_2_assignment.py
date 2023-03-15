"""Write a program to sort list of strings (similar to that of dictionary)"""

def sort_strings(lst):
    # iterate through the list and split each string into a list of words
    lst_of_words = [s.split() for s in lst]

    # sort the list of words using the first word as the key
    sorted_lst_of_words = sorted(lst_of_words, key=lambda x: x[0])

    # join the sorted list of words back into strings
    sorted_lst = [' '.join(words) for words in sorted_lst_of_words]

    return sorted_lst

# get user input for the list of strings
lst = input("Enter the list of strings to be sorted: ").split(', ')

# perform the sort
sorted_lst = sort_strings(lst)

# print the sorted list
print("Sorted list:", sorted_lst)
