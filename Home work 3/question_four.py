'''
Question: Given processes [p1, p2, ..., p_n] with respective starting times [r1, r2, ..., rn]

Calculate the optimal average time it takes to complete all the processes.
Note: The processes can preempt.
'''

import heapq

def get_optimal_schedule(tasks):
  # Sort tasks by their arrival times
  tasks = sorted(tasks, key=lambda x: x[1])

  # Initialize heap and completion time
  heap = []
  completion_time = 0
  result = []

  # Iterate through each task and update the heap and completion time
  for task in tasks:
    # If there are tasks in the heap and the next task arrives after the completion time of the current task
    if heap and task[1] >= completion_time:
      # Get the task with the shortest processing time from the heap
      p, start_time = heapq.heappop(heap)
      # Update the completion time
      completion_time += p
      # Add the task to the result
      result.append((start_time, completion_time))
    # Add the current task to the heap
    heapq.heappush(heap, (task[0], task[1]))

  # Process any remaining tasks in the heap
  while heap:
    p, start_time = heapq.heappop(heap)
    completion_time += p
    result.append((start_time, completion_time))

  return result


p = [10, 4, 6, 2, 8]
r = [0, 3, 4, 6, 7]
tasks = [(p[i],r[i]) for i in range(len(p))]
print(get_optimal_schedule(tasks))

