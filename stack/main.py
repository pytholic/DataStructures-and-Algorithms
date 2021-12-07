"""
How to manage browser back function (history) by using 
list-based stack in Python
"""

### Using List ###

# s = []
# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')

# print(s.pop())
# print(s)
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s)


### Using Deque ###
# from collections import deque

# stack = deque()
# #print(dir(stack))

# stack.append('https://www.cnn.com/')
# stack.append('https://www.cnn.com/world')
# stack.append('https://www.cnn.com/india')
# stack.append('https://www.cnn.com/china')

# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack)


### Pythonic Implementation of Stack ###

from collections import deque

class Stack:
	def __init__(self):
		self.container = deque()

	def push(self, val):
		self.container.append(val)

	def pop(self):
		return self.container.pop()

	def peek(self):
		return self.container[-1]

	def is_empty(self):
		return len(self.container) == 0

	def size(self):
		return len(self.container)

	def items(self):
		return (self.container)


s = Stack()
s.push(5)
s.push(10)
print(s.size())

print(s.items())
print(s.peek()) # Gives last value but doesn't removes it from stack
print(s.items())


print(s.pop()) # Gives last value and also removes it from stack
print(s.items())

print(s.pop()) # Gives last value and also removes it from stack
print(s.items())

print(s.is_empty())