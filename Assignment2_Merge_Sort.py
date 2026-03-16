import time
import random
import tracemalloc

# ---- MERGE SORT ----
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ---- QUICK SORT ----
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ---- PERFORMANCE MEASUREMENT ----
def measure_performance(sort_func, arr):
    tracemalloc.start()
    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time = end_time - start_time
    memory_used = peak / 1024  # Convert to KB
    return execution_time, memory_used

# ---- DATASETS ----
n = 1000
sorted_data = list(range(n))
reverse_sorted_data = list(range(n, 0, -1))
random_data = random.sample(range(n * 10), n)

datasets = {
    "Sorted Data": sorted_data,
    "Reverse Sorted Data": reverse_sorted_data,
    "Random Data": random_data
}

# ---- RUN AND PRINT RESULTS ----
print(f"{'Dataset':<25} {'Algorithm':<15} {'Time (seconds)':<20} {'Memory (KB)':<15}")
print("-" * 75)

for dataset_name, data in datasets.items():
    for sort_name, sort_func in [("Merge Sort", merge_sort), ("Quick Sort", quick_sort)]:
        exec_time, memory = measure_performance(sort_func, data)
        print(f"{dataset_name:<25} {sort_name:<15} {exec_time:<20.6f} {memory:<15.2f}")
