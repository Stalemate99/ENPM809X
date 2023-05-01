from typing import List
from sortedcollections import OrderedSet

class ContactNode:
  def __init__(self, src: int, dst: int, owlt: float, start: float = 0, end: float = float('inf'), pred = None, visited: bool = False, visited_nodes: List[int] = OrderedSet(), arrival_time:float = float('inf')) -> None:
    self.src = int(src)
    self.dst = int(dst)
    self.start = float(start)
    self.end = float(end)
    self.owlt = float(owlt)
    self.pred = pred
    self.visited = visited
    self.visited_nodes = visited_nodes
    self.arr_time = arrival_time

  def print(self):
    print(self.src,"->",self.dst," From:",self.start," To:",self.end," BDT:",self.arr_time," Visited Nodes:",self.visited_nodes)