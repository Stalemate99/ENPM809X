# Implementing min binary heap
from heapq import heapify, heappop, heappush

def extract_min(arr):
    heapify(arr)
    return heappop(arr)

arr = [1, 3, 5, 6, 3, 2, 7, 9, 4, 8]

print(extract_min(arr))