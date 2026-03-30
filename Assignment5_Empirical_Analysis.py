"""
Empirical Analysis - Deterministic vs Randomized Quicksort
Assignment 5 - Quicksort Algorithm
"""

import random
import time
import sys
import json

sys.setrecursionlimit(100000)

# ──────────────────────────────────────────────
# Deterministic Quicksort
# ──────────────────────────────────────────────
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def det_sort(arr):
    a = arr.copy()
    quicksort(a, 0, len(a) - 1)
    return a

# ──────────────────────────────────────────────
# Randomized Quicksort
# ──────────────────────────────────────────────
def randomized_partition(arr, low, high):
    r = random.randint(low, high)
    arr[r], arr[high] = arr[high], arr[r]
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

def rand_sort(arr):
    a = arr.copy()
    randomized_quicksort(a, 0, len(a) - 1)
    return a

# ──────────────────────────────────────────────
# Timing helper
# ──────────────────────────────────────────────
def measure(sort_fn, arr, runs=3):
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        sort_fn(arr)
        times.append(time.perf_counter() - start)
    return round(min(times) * 1000, 4)   # ms, best of 3

# ──────────────────────────────────────────────
# Run experiments
# ──────────────────────────────────────────────
sizes       = [100, 500, 1000, 3000, 5000]
distributions = ["random", "sorted", "reverse"]

results = {d: {"sizes": sizes, "det": [], "rand": []} for d in distributions}

for dist in distributions:
    for n in sizes:
        if dist == "random":
            arr = [random.randint(0, 10 * n) for _ in range(n)]
        elif dist == "sorted":
            arr = list(range(n))
        else:
            arr = list(range(n, 0, -1))

        # Deterministic — skip large sorted/reverse (stack overflow risk)
        if dist in ("sorted", "reverse") and n > 2000:
            det_time = None
        else:
            det_time = measure(det_sort, arr)

        rand_time = measure(rand_sort, arr)

        results[dist]["det"].append(det_time)
        results[dist]["rand"].append(rand_time)

        label = f"n={n:5d}"
        det_str  = f"{det_time:8.3f} ms" if det_time is not None else "  OVERFLOW"
        rand_str = f"{rand_time:8.3f} ms"
        print(f"[{dist:8s}] {label}  |  det={det_str}  |  rand={rand_str}")

print(json.dumps(results))
