class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_lst(self):
        temp = self.head

        while(temp):
            print(temp.data, "-->", end=" ")
            temp = temp.next
        print("None")

    def add_element_at_start(self, ele):
        first = Node(ele)
        first.next = self.head
        self.head = first

    def add_element_at_last(self, ele):
        newNode = Node(ele)

        last = self.head

        while(last.next != None):
            last = last.next

        last.next = newNode


l1 = LinkedList()

l1.head = Node(5)
n2 = Node(6)
n3 = Node(7)

l1.head.next = n2
n2.next = n3

l1.print_lst()
l1.add_element_at_start(4)
l1.print_lst()

print("Adding last")
l1.add_element_at_last(8)
l1.print_lst()

print("hello")

