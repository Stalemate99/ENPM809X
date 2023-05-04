class MinHeap:
  def __init__(self) -> None:
    self.size = 0
    self.heap = [0]

  def min_heapify(self, index) -> None:
    left = 2 * index
    right = left + 1

    if left <= self.size and self.heap[left].arr_time < self.heap[index].arr_time:
      min_index = left
    else:
      min_index = index

    if right <= self.size and self.heap[right].arr_time < self.heap[min_index].arr_time:
      min_index = right

    if min_index != index:
      self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
      self.min_heapify(min_index)

  def extract_min(self) -> int:
    if self.size <= 0:
      return None

    if self.size == 1:
      self.size -= 1
      return self.heap.pop(-1)

    min_ele = self.heap[1]
    self.heap[1] = self.heap.pop(-1)
    self.size -= 1
    self.min_heapify(1)
    return min_ele

  def decrease_key(self, index, key) -> None:
    self.heap[index] = key
    parent = index // 2
    while index > 1 and self.heap[index].arr_time < self.heap[parent].arr_time:
      self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
      index = parent
      parent = index // 2

  def insert(self, c_node) -> None:
    self.size += 1
    self.heap.append(float('inf'))
    self.decrease_key(self.size, c_node)