"""
Deterministic Quicksort Implementation
Assignment 5 - Quicksort Algorithm
"""

def partition(arr, low, high):
    """
    Partitions the array around a pivot (last element).

    - Elements smaller than pivot go to the LEFT
    - Elements greater than pivot go to the RIGHT
    - Pivot is placed at its correct sorted position

    Args:
        arr  : The list to partition
        low  : Starting index of the subarray
        high : Ending index of the subarray (pivot index)

    Returns:
        pivot_index : The final position of the pivot
    """
    pivot = arr[high]       # Choose the last element as pivot
    i = low - 1             # i tracks the boundary of smaller elements

    for j in range(low, high):
        # If current element is less than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1            # Return the pivot's final index


def quicksort(arr, low, high):
    """
    Recursively sorts the array using the Quicksort algorithm.

    Args:
        arr  : The list to sort
        low  : Starting index
        high : Ending index
    """
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after the pivot
        quicksort(arr, low, pivot_index - 1)   # Left subarray
        quicksort(arr, pivot_index + 1, high)  # Right subarray


def sort(arr):
    """
    Helper function to call quicksort on the full array.

    Args:
        arr : The list to sort

    Returns:
        arr : Sorted list (in-place)
    """
    quicksort(arr, 0, len(arr) - 1)
    return arr


# -------------------------
# Test the Implementation
# -------------------------
if __name__ == "__main__":
    test_cases = {
        "Random Array"        : [10, 7, 8, 9, 1, 5],
        "Already Sorted"      : [1, 2, 3, 4, 5, 6],
        "Reverse Sorted"      : [6, 5, 4, 3, 2, 1],
        "Array with Duplicates": [3, 6, 8, 10, 1, 2, 1],
        "Single Element"      : [42],
        "Empty Array"         : [],
    }

    for label, arr in test_cases.items():
        result = sort(arr.copy())
        print(f"{label:25} => {result}")
