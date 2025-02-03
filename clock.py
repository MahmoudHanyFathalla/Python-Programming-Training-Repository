import time
import random
import numpy as np
import matplotlib.pyplot as plt

# BFPRT Algorithm
def bfprt(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    medians = [sorted(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(0, len(arr), 5)]
    pivot = bfprt(medians, len(medians)//2)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return bfprt(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return bfprt(highs, k - len(lows) - len(pivots))

# Sorting-Based Selection
def sort_and_select(arr, k):
    return sorted(arr)[k]

# Experimental Setup
array_sizes = [100, 1000, 10000, 100000, 1000000]
results_sorting = []
results_bfprt = []

for n in array_sizes:
    arr = [random.randint(1, n) for _ in range(n)]
    k = n // 2  # Median
    # Measure Sorting-Based Time
    start = time.time()
    sort_and_select(arr, k)
    end = time.time()
    results_sorting.append(end - start)

    # Measure BFPRT Time
    start = time.time()
    bfprt(arr, k)
    end = time.time()
    results_bfprt.append(end - start)

# Plot Results
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, results_sorting, label='Sorting-Based Selection', marker='o')
plt.plot(array_sizes, results_bfprt, label='BFPRT Selection', marker='x')
plt.xlabel('Array Size (n)')
plt.ylabel('Runtime (seconds)')
plt.title('Performance Comparison: Sorting vs BFPRT')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()
