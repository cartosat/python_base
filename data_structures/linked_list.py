# Create node class
class Node:
    # Each node will have data and pointer, so added those variables in constructor.
    def __init__(self, data):
        self.data = data
        self.next = None

# Now we need another class linkedList.
class LinkedList:
    def __init__(self):
        self.head = None

# Created object of linkedlist.
llist = LinkedList()
# Assigned reference of Node to linkedList
llist.head = Node(1)

# Creating another nodes
second = Node(12)
third = Node(16)

# Adding references or pointers to next node.
llist.head.next = second
second.next = third

# You can set debugger at print statement and observe linkedlist.
print("Ok")