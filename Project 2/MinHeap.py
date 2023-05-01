class MinHeap:
  def __init__(self) -> None:
    self.size = 0
    self.heap = [0]

  def shift_up(self, index) -> None:
    flag = False
    while (index//2 > 0) and not flag:
      if self.heap[index].arr_time < self.heap[index//2].arr_time:
        self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
      else:
        flag = True
      index = index // 2

  def insert(self, c_node) -> None:
    self.heap.append(c_node)
    self.size += 1
    self.shift_up(self.size)