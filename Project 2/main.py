import os

from ContactGraph import ContactGraph
from ContactNode import ContactNode
from Routing import CGR

# Reading contents from input file
input_filename = "ContactList.txt"
input_file = os.path.join(os.path.dirname(__file__), input_filename)

# Initializing the contact plan
contact_graph = ContactGraph()

# Populating the file contents into contact plan
with open(input_file,'r') as file:
  for line in file:
    id, start_time, end_time, src, dst, owlt = line.split(' ')
    contact_graph.add_record(int(id), ContactNode(int(src), int(dst), float(owlt), float(start_time), float(end_time)))

# Initialize root contact and final destination
root = contact_graph.get_root()
dest_contact = 12

route, time = CGR(contact_graph, root, dest_contact)

print("The shortest path involved visiting the following contacts ::",list(route))
print("The shortest arrival time ::", time)