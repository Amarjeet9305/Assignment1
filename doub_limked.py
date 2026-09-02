class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create nodes
node1 = Node(29)
node2 = Node(72)
node3 = Node(84)

# Connect nodes
node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

# Insert a element in particular b/w 72 and 84 insert element 25
# Create a new node

new_node = Node(25)

# Step1:
new_node.next = node2.next

# Step2: connect back 25 to 72

new_node.prev = node2

# Step4: connect 72 to 25

node2.next.prev = new_node

# Step5: 
node2.next = new_node

# Forward traversal
current = node1

while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")