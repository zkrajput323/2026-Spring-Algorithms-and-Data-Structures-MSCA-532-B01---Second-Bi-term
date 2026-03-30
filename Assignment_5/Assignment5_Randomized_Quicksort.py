"""
Randomized Quicksort Implementation
Assignment 5 - Quicksort Algorithm
"""

import random


def partition(arr, low, high):
    """
    Partitions the array around a pivot (last element after random swap).

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
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_partition(arr, low, high):
    """
    Picks a RANDOM pivot from the subarray [low..high],
    swaps it to the last position, then calls regular partition.

    This ensures no specific input pattern can consistently
    trigger the O(n²) worst case.

    Args:
        arr  : The list to partition
        low  : Starting index
        high : Ending index

    Returns:
        pivot_index : Final position of the pivot
    """
    random_pivot_index = random.randint(low, high)          # Pick random index
    arr[random_pivot_index], arr[high] = arr[high], arr[random_pivot_index]  # Swap to end
    return partition(arr, low, high)                        # Partition normally


def randomized_quicksort(arr, low, high):
    """
    Recursively sorts the array using Randomized Quicksort.

    Args:
        arr  : The list to sort
        low  : Starting index
        high : Ending index
    """
    if low < high:
        pivot_index = randomized_partition(arr, low, high)

        randomized_quicksort(arr, low, pivot_index - 1)    # Left subarray
        randomized_quicksort(arr, pivot_index + 1, high)   # Right subarray


def sort(arr):
    """
    Helper function to call randomized_quicksort on the full array.

    Args:
        arr : The list to sort

    Returns:
        arr : Sorted list (in-place)
    """
    randomized_quicksort(arr, 0, len(arr) - 1)
    return arr


# -------------------------
# Test the Implementation
# -------------------------
if __name__ == "__main__":
    test_cases = {
        "Random Array"         : [10, 7, 8, 9, 1, 5],
        "Already Sorted"       : [1, 2, 3, 4, 5, 6],
        "Reverse Sorted"       : [6, 5, 4, 3, 2, 1],
        "Array with Duplicates": [3, 6, 8, 10, 1, 2, 1],
        "Single Element"       : [42],
        "Empty Array"          : [],
    }

    print("=" * 55)
    print("  Randomized Quicksort - Test Results")
    print("=" * 55)
    for label, arr in test_cases.items():
        result = sort(arr.copy())
        print(f"  {label:25} => {result}")
    print("=" * 55)
