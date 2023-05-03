from typing import List

from ContactGraph import ContactGraph
from ContactNode import ContactNode

"""
Contact Graph Route
Modified Dijkstra algorithm to find the shorted arrival time from the given source

params
graph - Contact Graph's plan
root - Starting/Source node
dest - Final destination value

return
route - List of visited nodes in shortest path
time - Shortest arrival time
"""
def CGR(graph: ContactGraph, root: ContactNode, dest: int):
    bdt = float('inf') # Minimum arrival time
    final_contact = None
    curr_contact = root

    while True:
        # Relaxing valid neighbours of current cotact
        final_contact, bdt = CRP(graph, curr_contact, final_contact, bdt, dest)

        # Selecting the next neightbour with the smallest arrival time
        curr_contact = CSP(graph, bdt)

        # Exit condition
        if not curr_contact:
          break

    return (final_contact.visited_nodes, bdt)

"""
Contact Review Procedure
Modified relaxation algorithm to update the arrival times of the neighbouring contacts

params
graph - Contact Graph's plan
curr_contact - Current contact
final_contact - Final possible contact [Will contain the node before the destination node]
bdt - current shortest arrival time
final_dest - Final destination value

return
final_contact
bdt
"""
def CRP(graph: ContactGraph, curr_contact: ContactNode, final_contact: ContactNode, bdt: float, final_dest: int):
    contact_plan = graph.plan

    for _, contact in contact_plan.items():
      # Checking for possible neighbouring contacts
      if curr_contact.dst == contact.src:
        if contact.end <= curr_contact.arr_time or contact.dst in curr_contact.visited_nodes:
          continue

        # Trying tro relax the arrival time of neighbours
        if contact.start < curr_contact.arr_time:
          arr_time = curr_contact.arr_time + contact.owlt
        else:
          arr_time = contact.start + contact.owlt

        # If calculated arrival time is lesser than the existing arrival time,
        # update the contact with new arrival time
        if arr_time < contact.arr_time:
          contact.arr_time = arr_time
          contact.pred = curr_contact
          curr_contact.visited_nodes.add(contact.src)
          contact.visited_nodes = curr_contact.visited_nodes

          # If next contact has the destination node with better BDT,
          # return the final contact and updated BDT
          if contact.dst == final_dest and contact.arr_time < bdt:
            bdt = contact.arr_time
            final_contact = contact

    # Mark the current node as visited for future reference
    curr_contact.visited = True
    return final_contact, bdt

"""
Contact Selection Procedure
Find the next shortest contact that is not part of the visited contacts

params
graph - Contact Graph's plan
bdt - current shortest arrival time

return
next_contact - Contact with the next shortest arrival among the neighbouring contacts. Can be None.
"""
def CSP(graph: ContactGraph, bdt: float) -> ContactNode:
    next_contact = None
    best_arr = float('inf')

    contact_plan = graph.plan
    for _, contact in contact_plan.items():
        if contact.arr_time > bdt or contact.visited:
            continue

        if contact.arr_time < best_arr:
            best_arr = contact.arr_time
            next_contact = contact

    return next_contact