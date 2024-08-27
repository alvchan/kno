"""
Binary Search Ex [binary_search.py]
    Sample code for a binary search implementation in an ordered array.
"""

def binary_search(arr, target):
    lower_bound = 0
    upper_bound = len(arr) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2

        # play your game of "higher or lower" until target is cornered
        if target < arr[midpoint]:
            upper_bound = midpoint - 1
        elif target > arr[midpoint]:
            lower_bound = midpoint + 1
        elif target == arr[midpoint]:
            return midpoint

    # target not in list
    return None

print(binary_search([1,2,3], 3))
