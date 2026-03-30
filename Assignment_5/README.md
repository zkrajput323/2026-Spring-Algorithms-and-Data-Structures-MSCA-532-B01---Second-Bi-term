# Assignment 5: Quicksort Algorithm
### Implementation, Analysis, and Randomization

---

## Overview

This repository contains the full implementation and empirical analysis of the **Quicksort algorithm** in Python — both a deterministic and a randomized version. It includes:

- Deterministic Quicksort (fixed last-element pivot)
- Randomized Quicksort (random pivot selection)
- Empirical performance comparison across different input types
- A full written report with theoretical analysis

---

## Repository Structure

```
├── quicksort.py                  # Deterministic Quicksort implementation
├── randomized_quicksort.py       # Randomized Quicksort implementation
├── empirical_analysis.py         # Performance comparison script
└── README.md                     # This file
```

---

## How to Run

### Prerequisites
- Python 3.7 or higher
- No external libraries required

### 1. Run Deterministic Quicksort
```bash
python quicksort.py
```
**Expected output:**
```
Random Array              => [1, 5, 7, 8, 9, 10]
Already Sorted            => [1, 2, 3, 4, 5, 6]
Reverse Sorted            => [1, 2, 3, 4, 5, 6]
Array with Duplicates     => [1, 1, 2, 3, 6, 8, 10]
Single Element            => [42]
Empty Array               => []
```

### 2. Run Randomized Quicksort
```bash
python randomized_quicksort.py
```
**Expected output:**
```
=======================================================
  Randomized Quicksort - Test Results
=======================================================
  Random Array              => [1, 5, 7, 8, 9, 10]
  Already Sorted            => [1, 2, 3, 4, 5, 6]
  Reverse Sorted            => [1, 2, 3, 4, 5, 6]
  Array with Duplicates     => [1, 1, 2, 3, 6, 8, 10]
  Single Element            => [42]
  Empty Array               => []
=======================================================
```

### 3. Run Empirical Analysis
```bash
python empirical_analysis.py
```
This will benchmark both algorithms on:
- **Random** arrays
- **Sorted** arrays
- **Reverse-sorted** arrays

Across input sizes: `n = 100, 500, 1000, 3000, 5000`

> **Note:** The deterministic version may produce a `RecursionError` (stack overflow) on sorted/reverse-sorted inputs at n > 2000. This is expected and demonstrates the O(n²) worst case.

---

## Key Findings

| Input Type | Deterministic | Randomized | Winner |
|---|---|---|---|
| Random | O(n log n) ✅ | O(n log n) ✅ | Tie (det. slightly faster) |
| Sorted | O(n²) ❌ | O(n log n) ✅ | Randomized |
| Reverse-sorted | O(n²) ❌ | O(n log n) ✅ | Randomized |

### Sample Empirical Results (Sorted Input)

| n | Deterministic | Randomized |
|---|---|---|
| 100 | 0.351 ms | 0.069 ms |
| 500 | 9.021 ms | 0.483 ms |
| 1000 | 38.441 ms | 1.157 ms |
| 3000 | OVERFLOW 💥 | 3.727 ms |
| 5000 | OVERFLOW 💥 | 6.586 ms |

---

## Algorithm Summary

### Deterministic Quicksort
- **Pivot:** Always the last element of the subarray
- **Best/Average Case:** O(n log n)
- **Worst Case:** O(n²) — triggered by sorted or reverse-sorted input
- **Space:** O(log n) average, O(n) worst case (call stack)

### Randomized Quicksort
- **Pivot:** Randomly selected from the subarray, then swapped to the end
- **Expected Time:** O(n log n) for ALL input types
- **Worst Case:** Astronomically unlikely — probability ≈ (2/n)^n
- **Space:** O(log n) average

### The Only Code Difference
```python
# Deterministic — pivot is always the last element
pivot = arr[high]

# Randomized — pivot is randomly chosen
r = random.randint(low, high)
arr[r], arr[high] = arr[high], arr[r]  # swap to end, then partition normally
```

---

## Time Complexity Analysis

```
Best Case:    O(n log n)  →  Pivot splits array 50/50 every time
Average Case: O(n log n)  →  Random input, expected balanced splits  
Worst Case:   O(n²)       →  Sorted/reverse-sorted + last-element pivot
```

**Why O(n log n) on average?**  
At each level of the recursion tree, all partition calls together process exactly `n` elements. With balanced splits, the tree has `log n` levels. Therefore: `n × log n = O(n log n)`.

**Why O(n²) in the worst case?**  
With unbalanced splits (one side always empty), the recursion depth reaches `n`. The total work sums to: `n + (n-1) + ... + 1 = n(n+1)/2 = O(n²)`.

---

## Conclusion

Randomized Quicksort is the recommended implementation for real-world use. A simple two-line change — choosing a random pivot — eliminates input-dependent worst-case behavior entirely, delivering consistent O(n log n) performance across all input distributions with negligible overhead.

---

## References

- Cormen, T. H., et al. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
- Hoare, C. A. R. (1962). Quicksort. *The Computer Journal*, 5(1), 10–16.
- Python Software Foundation. (2024). `time` — Time access and conversions. Python 3 Documentation.
