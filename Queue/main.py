"""
Python queue implementation with list
"""

### Queue implementation with list ###

wmt_stock_price_queue = []

wmt_stock_price_queue.insert(0, 131.0)
wmt_stock_price_queue.insert(0, 125.0)
wmt_stock_price_queue.insert(0, 120.0)

print(wmt_stock_price_queue.pop())
print(wmt_stock_price_queue.pop())
print(wmt_stock_price_queue.pop())


### Queue implementation with deque ###

from collections import deque
q = deque()

q.appendleft(5)
q.appendleft(10)
q.appendleft(15)

print(q.pop())
print(q.pop())
print(q.pop())


### Implementing Queue class ###
class Queue:

	def __init__(self):
		self.buffer = deque()

	def enqueue(self, val):  # Placing an element in the queue
		return self.buffer.appendleft(val)

	def dequeue(self):  # removing an element in the queue	
		return self.buffer.pop()

	def is_empty(self):
		return len(self.buffer) == 0

	def size(self):
		return len(self.buffer)


pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.buffer)

print(pq.dequeue())

print(pq.size())