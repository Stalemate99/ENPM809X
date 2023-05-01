from collections import defaultdict

from ContactNode import ContactNode

class ContactGraph:
  def __init__(self, plan: ContactNode = defaultdict()) -> None:
    self.plan = plan

  def get_record(self, id: int) -> ContactNode:
    return self.plan[id]

  def add_record(self, id: int, record: ContactNode) -> None:
    self.plan[id] = record

  def get_root(self) -> ContactNode:
    return ContactNode(1,1,0,0,float('inf'),visited=True,arrival_time=0)