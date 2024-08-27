"""
Linear Search Ex [linear_search.py]
    A sample code for implementing linear search for an ordered array.
"""

def linear_search(arr, target):
    for i, x in enumerate(arr):
        # keep checking until target is found
        if (x == target):
            return (x, i)
        # next val larger than target, thus next cannot be the target (ord arr)
        elif (x > target):
            break

    # given target not in arr, return as such
    return None

x, i = linear_search([1,2,3], 3)
print(f"{x} at index {i}")
