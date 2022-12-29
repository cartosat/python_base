# We can implement a stack in Python in the following ways.
# 		- List --> we can use append as push and list have built in pop function.
# 		- dequeu --> collections module provides the deque class,
# 	                	which is used to creating Python stacks.
#                   - The deque can be preferred over the list because it performs
#                       append and pop operation faster than the list.
#                   -  The time complexity is O(1), where the list takes O(n).
# 		- LifeQueue --> The queue module has the LIFO queue, which is the same as the stack.
#                    - We can add elements by put() function and remove them with get().
#
#  - Let us cleat the confusion; we are using stack with the threading, you should use the
#       Lifoqueue but make sure about its performance for popping and pushing elements.
#  - But if you are not using threading, use a deque.
#

# Using List

my_stack = []

my_stack.append("V")
my_stack.append("a")
my_stack.append("i")

print(my_stack)

# Last pushed element i.e 'i' is popped.
my_stack.pop()
print(my_stack)

# using collections.deque

from collections import deque

my_stack2 = deque()

my_stack2.append('S')
my_stack2.append('w')
my_stack2.append('a')

print(my_stack2)

# Last pushed element i.e 'a' is popped.
my_stack2.pop()
print(my_stack2)

# Using queue module

from queue import LifoQueue

my_stack3 = LifoQueue()

my_stack3.put('V')
my_stack3.put('i')
my_stack3.put('d')

print(my_stack3.qsize())

# Last pushed element is popped using get method.
my_stack3.get()
print(my_stack3.qsize())
