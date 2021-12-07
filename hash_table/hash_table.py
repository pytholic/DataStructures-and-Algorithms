
# stock_prices = []
# with open("stock_prices.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_prices.append([day,price])

# print(stock_prices)

# # Complexity of search using a list is O(n)

# for element in stock_prices:
#     if element[0] == '9-Mar':
#         print(element[1])


# stock_prices = {}
# with open("stock_prices.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_prices[day] = price

# # Complexity of search using a list is O(1)

# print(stock_prices)
# print(stock_prices['9-Mar'])


### IMPLEMENTING HASH TABLE IN PYTHON ####

# def get_hash(key):
# 	h = 0
# 	for char in key:
# 		h += ord(char) # ord func return ascii  value of the char
# 	return  h % 100

# print(get_hash('6-Mar'))


# Creating a hash table

class HashTable:
	def __init__(self):
		self.MAX = 100
		self.arr = [None for i in range(self.MAX)] # list comprehension initialization

	# Function to get hash value
	def get_hash(self, key):
		h = 0
		for char in key:
			h += ord(char)
		return h % self.MAX

	# Function to add an item into hash map
	# def add(self, key, val):
	# 	h = self.get_hash(key)
	# 	self.arr[h] = val

	def __setitem__(self, key, val):
		h = self.get_hash(key)
		self.arr[h] = val

	# Function to get an item from hash map
	# def get(self, key):
	# 	h = self.get_hash(key)
	# 	return self.arr[h]

	def __getitem__(self, key):
		h = self.get_hash(key)
		return self.arr[h]
 

	# Function to del item
	def __delitem__(self, key):
		h = self.get_hash(key)
		self.arr[h] = None


table = HashTable()
#print(table.get_hash('6-Mar'))

# # Testing add function
# table.add('6-Mar', 130)
# print(table.arr)
# print(table.arr.index(130))

# # Testing get function
# print(table.get('6-Mar'))

# Testing setitem function
# table['6-Mar'] = 130
# print(table['6-Mar'])

# # Testing getitem function
# print(table['6-Mar']) # will throw an error in getitem is not implemented

table["6-Mar"] = 310
table["7-Mar"] = 420
table["6-Nov"] = 333
table["7-Dec"] = 231
print(table['7-Mar'])
print(table['6-Nov'])
print(table['16-Mar'])

# Testing delitem function
del table['6-Mar']
print(table['6-Mar'])