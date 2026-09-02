# Creating a Node

class Node:
    def __init__(self,data):
        self.data = data    # Store the value
        self.next = None    # Store the reference to the next node
        
class LinkedList:
    def __init__():
        self.head = None    # Keeps track of the start of the list
        
# Create a node

node1=Node(25)
node2 = Node(35)
node3 = Node(45)
node4 = Node(55)

# Link the each of node
node1.next = node2  # Node1 to point Node 2 address
node2.next = node3
node3.next = node4

# Set the head node
head = node1        


# make a temporary pointer

current = head

while current is not None:
    print(current.data, end=" -> ")
    current = current.next   # move next node
print("None") 