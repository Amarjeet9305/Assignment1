class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
# First create a node

node1 = Node(10)
node2 = Node(20) 
node3 = Node(25) 
node4 = Node(30)        


# Connect each of node

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

# Delete node3 (25)

# Connect node 20 to 30

node3.prev.next = node3.next

# Again 30 back to 20 connect

node3.next.prev = node3.prev

# Forward traversal

current = node1

while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")    