import random
import os
import time
import matplotlib.pyplot as plt

def fuzzy_sort(intervals):
    # Helper function to partition the intervals around a pivot
    def partition(intervals, left, right):
      pivot_index = random.randint(left, right)
      pivot = intervals[pivot_index][0]

      # Swap the pivot with the rightmost element
      intervals[pivot_index], intervals[right] = intervals[right], intervals[pivot_index]

      # Partition the list around the pivot
      i = left - 1
      for j in range(left, right):
        if intervals[j][0] <= pivot:
          i += 1
          intervals[i], intervals[j] = intervals[j], intervals[i]

      intervals[i+1], intervals[right] = intervals[right], intervals[i+1]
      return i+1

    # Recursive helper function to perform the quicksort
    def quicksort(intervals, left, right):
      if left < right:
        pivot = partition(intervals, left, right)
        quicksort(intervals, left, pivot-1)
        quicksort(intervals, pivot+1, right)

    # Sort the intervals by their left endpoint (a)
    quicksort(intervals, 0, len(intervals)-1)

    # Merge overlapping intervals
    merged_intervals = []
    current_interval = intervals[0]

    for i in range(1, len(intervals)):
      # Check if the current interval overlaps with the next interval
      if current_interval[1] >= intervals[i][0]:
        current_interval = (current_interval[0], max(current_interval[1], intervals[i][1]))
      else:
        merged_intervals.append(current_interval)
        current_interval = intervals[i]

    merged_intervals.append(current_interval)

    return merged_intervals


all_overlap_filename = 'all_overlap.txt'
small_overlap_filename = "small_overlap.txt"
small_overlap_file = os.path.join(os.path.dirname(__file__), small_overlap_filename)
all_overlap_file = os.path.join(os.path.dirname(__file__), all_overlap_filename)

intervals = []
x,y = [],[]

with open(all_overlap_file,'r') as file:
  for line in file:
    intervals.append([float(x) for x in line.split(' ')])


for i in range(1000,len(intervals),2000):
  start_time = time.perf_counter()
  result = fuzzy_sort(intervals[:i])
  end_time = time.perf_counter()
  # print(len(intervals[:i]))
  x.append(i)
  y.append(end_time - start_time)

plt.plot(x,y)
plt.xlabel('Number of Intervals')
plt.ylabel('Execution Time')
plt.title("All Overlap File")
plt.show()