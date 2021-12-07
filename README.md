# Data Structures and Algorithms

## Big O Notation
When it comes to `problem-solving`, `programming interviews` or `algorithms`, **Big O Notation** is probably one of the most important concepts.

For example, take an example of sorting list/array element i.e. *a = ['C', 'B', 'A']*. Now there can be tons of ways to perform this task. Some are going to be better than the others, some are going to be quicker and some are going to take more space.
As the input size grows, the nit becomes important to consider how these different sorting algorithms `scale` with the input size. Understanding all of these concepts is important to write **efficient code**.

All of these different thought considerations around `speed` and `memory usage` are what **Big O Notation** is built around. The idea of Big O Notation is analyzing the algorithm that you create. How **long** your algorithm takes to execute and how much **space** does it take. Not only considering whether my algorithm will become slower and take more space as input scales but also thinking about **how much slower** will it become and **how much more space** will it require compared to other similar algorithms based on the same set of inputs.

Look at the `big_o.py` for some code examples. Also check out this [link](https://www.youtube.com/watch?v=itn09C2ZB9Y) for better understanding.


---
## List
A **list** is a data structure that's built into Python and holds a collection of items. 

* List items are enclosed in square brackets, like this [item1, item2, item3].
* Lists are **ordered** – i.e. the items in the list appear in a specific order. This enables us to use an index to access any item.
* Lists are **mutable**, which means you can add or remove items after a list's creation.
* List elements **do not need to be unique**. Item duplication is possible, as each element has its distinct place and can be accessed separately through the index.
* Elements can be of **different data types**: you can combine strings, integers, and objects in the same list.

Lists are very easily created in Python:

**Code**
```python
list = [3, 6, 9, 12]
print(list)
print(type(list))
```

**Output**
```
[3, 6, 9, 12]
<class 'list'>
```

---
## Array
An **array** is also a data structure that stores a collection of items. Like lists, arrays are **ordered, mutable, enclosed in square brackets**, and able to store **non-unique** items.

But when it comes to the array's ability to store different data types, the answer is not as straightforward. It depends on the kind of array used.

To use arrays in Python, you need to import either an `array module` or a `NumPy package`. I personally always use NumPy.

**Code**
```python
import array as arr
import numpy as np
```

The Python `array module` requires all array elements to be of the same type. Moreover, to create an array, you'll need to specify a value type. In the code below, the "i" signifies that all elements in array_1 are integers:

**Code**
```python
array_1 = arr.array("i", [3, 6, 9, 12])
print(array_1)
print(type(array_1))
```

**Output**
```
array('i', [3, 6, 9, 12])
<class 'array.array'>
```

On the other hand, `NumPy arrays` support different data types which is my preferred method. To create a NumPy array, you only need to specify the items (enclosed in square brackets, of course):

**Code**

```python
array_2 = np.array(["numbers", 3, 6, 9, 12])
print (array_2)
print(type(array_2))

```

**Output**
```
['numbers' '3' '6' '9' '12']
<class 'numpy.ndarray'>
```

As you can see, *array_2* contains one item of the *string* type (i.e., *"numbers"*) and four integers.

---
### List vs Array?
Now that we know their definitions and features, we can talk about the differences between lists and arrays in Python:

* **Arrays need to be declared**. Lists don't, since they are built into Python. In the examples above, you saw that lists are created by simply enclosing a sequence of elements into square brackets. Creating an array, on the other hand, requires a specific function from either the `array module` (i.e., *array.array()*) or `NumPy package` (i.e., *numpy.array()*). Because of this, lists are used more often than arrays.
  
* **Arrays can store data very compactly** and are more efficient for storing large amounts of data.
  
* **Arrays are great for numerical operations**; lists cannot directly handle math operations. For example, you can divide each element of an array by the same number with just one line of code. If you try the same with a list, you'll get an error.

**Code**
```python
array = np.array([3, 6, 9, 12])
division = array/3
print(division)
print (type(division))
```

**Output**
```
[1. 2. 3. 4.]
<class 'numpy.ndarray'>
```

**Code**
```python
list = [3, 6, 9, 12]
division = list/3
```

**Output**
```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
 in ()
      1 list = [3, 6, 9, 12]
----> 2 division = list/3

TypeError: unsupported operand type(s) for /: 'list' and 'int'
```

Of course, it's possible to do a mathematical operation with a list, but it's much less efficient:

---
## Linked List
**Linked list** is a data structure similar to an array in the sense that it stores a bunch of items. However, unlike an array, linked lists are not stored in **contiguous memory locations**. They are instead `chained` by an element storing the address location of `next element`.  This makes `insertion` very easy and efficient.

Also unlike **dynamic arrays** you don't have to `pre-allocate` some memory capacity. 

---
### Linked List vs Array
**Arrays** store elements in contiguous memory locations, resulting in easily calculable addresses for the elements stored and this allows **faster access** to an element at a `specific index`.

**Linked lists** are less rigid in their storage structure and elements are usually not stored in contiguous locations, hence they need to be stored with `additional tags` giving a **reference to the next element**. This difference in the data storage scheme decides which data structure would be more suitable for a given situation. 

Major differences are listed below: 

* **Size**: Since data can only be stored in contiguous blocks of memory in an array, **its size cannot be altered at runtime** due to the risk of `overwriting` other data. However, in a linked list, each **node points to the next one such that data** can exist at scattered (non-contiguous) addresses; this allows for a `dynamic size` that can change at runtime.

* **Memory allocation**: For arrays at `compile time` and at `runtime` for linked lists. but, a dynamically allocated array also allocates memory at runtime.

* **Memory efficiency**: For the same number of elements, linked lists use more memory as a reference to the next node is also stored along with the data. However, size flexibility in linked lists may make them use **less memory overall**; this is useful when there is uncertainty about size or there are large variations in the size of data elements; **memory equivalent to the upper limit on the size** has to be allocated (even if not all of it is being used) while using arrays, whereas linked lists can increase their sizes step-by-step proportionately to the amount of data.

* **Execution time**: Any element in an array can be directly accessed with its index; however in the case of a linked list, *all the previous elements must be traversed to reach any element*. Also, better cache locality in arrays (due to contiguous memory allocation) can significantly improve performance. As a result, some operations (such as modifying a certain element) are faster in arrays, while some others (such as inserting/deleting an element in the data) are faster in linked lists.

Following are the points in favor of Linked Lists. 

1. The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage, and in practical uses, the upper limit is rarely reached. Also, if the array is dynamic and size is increased during `runtime`, still the space allocated is fixed and we might not use all of it. So arrays are not `memory efficient` in this sense.
   
2. **`Inserting` a new element** in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted. **`Deletion`** is also expensive with arrays unless some special techniques are used.

---
## Hash Table
<<<<<<< HEAD
=======
A data type that stores **key, value** pairs. **Hash map/table** are internal data structure, and **Dictionary** is a python specific implementation of hash table.

* When you store data as a **2D list** in the memory, it stores data as contiguous memory locations on the RAM. 
* When you use **dictionary** on the other hand, the way it will store this data in RAM is first it will allocate a `list` of some size, and then it will map the first key to a specific element in that list. To get an index `index` of that element in that particular list, we use **Hash Function**.
* The purpose of a hash function is to convert our string key into an `index` in an array.
* Similarly we can apply the hash function for all other `keys`. Find out an `index` into an array, and store those elements at that index.

In **array**, we have integer index, while in **hash map** we can use string indexes.

```python
# Array
stock_prices[0]

# Dict
stock_prices['march 6']
```

### Example
To **find** a particular element in an **array/list**, we have to look through each element. So `complexity` is directly proportional to input size i.e. **`O(n)`**. This can be very inefficient if it contains millions of records.

**Code**
```python
'''
List / Array
'''

stock_prices = []
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])


# Finding price on a specific day
for element in stock_prices:
    if element[0] == '9-Mar':
        print(element[1])

```

Alternately, we can use **dictionaries** and perform the same operation with a complexity of the order of '1' i.e. **`O(1)`**

**Code**
```python
'''
Dictionary
'''

stock_prices_dict = {}
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices_dict[day] = price

#print(stock_prices_dict)
print(stock_prices_dict['9-Mar'])
```

### So how do we get index using **Hash Function**? What is this **Hash Function**?
There are different ways of implementing **hash function**. One was is using `ASCII` numbers.

We can take `each letter` in the input key, and find out the `ASCII` value for each letter. For example,

|letter| ASCII Code|        
|------|-----------|
|m     |109       |
|a     |97        |
|r     |114       |
|c     |99        |
|h     |104       |
|      |32        |
|6     |54        |
|SUM   |609       |

If we want to get an index between `0-9`, we can use `modulus` operation.

```
MOD(609, 10) -> 9 (where 10 is the size of the array)
```

### Time COmplexity
* **Look up** by key is `O(1)` on average
* **Insertion/Deletion** is `O(1)` on average

**Note:** In `worst case`, this complexity can be more than `O(1)`.

### Hash table in different languages
**Python -> dictionary**
```python
prices = {
      'march 6': 310,
      'march 7': 430
}
```

**JAVA -> Hashmap**
```java
HashMap<String, Integer> prices = new Hashmap<String, Integer>();

prices.put("march 6", 310)
prices.put("march 7", 430)
```

**JAVA -> LinkedHashmap**
```java
LinkedHashMap<String, Integer> prices = new LinkedHashmap<String, Integer>();

prices.put("march 6", 310)
prices.put("march 7", 430)
```

**C++ -> std::map**
```c++
stp::map<string, int> prices;

prices['match 6'] = 310
prices['match 7'] = 430
```

### Implementing Hash Map in Python
We create a manual class to implement **hash table** in python. We create some functions to get `ascii` hash values, `add` item to hash table and `get` an items value from has table.

Later, instead of add and get functions, we use python item operator functions i.e. `setitem` and `getitem` which allows us to override existing values and makes code more ncie and convenient.


**Code**

```python

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

```

By writing this class, we actually implemented a dictionary. Usually in programming we won't have to define these classes. However, writing it manually helps in understanding hash maps better.


### Collision Handling

**Collision:** Two keys trying to store value at the **same location**.
So, we need to handle these collisions.

#### METHOD 1: Chaining

We can use an approach called **chaining**. Instead of directly storing the value, we store a `linked-list` or a list at every location. This list can keep on growing and multiple keys can share the same hash value.

However, our **complexity** now can grow from `O(1)` to `O(n)` i.e. when we have a bad hashing function and all the keys generate the same index. Then all of our values will be stuck in one list.

In that case search complexity will be same as of a linked-list which is `O(n)`. Because after getting hash value, we have to linearly search through whole list.

For that reason, it is important to have our `key` stored in each of these elements. So that we know which value is associated with which key.

#### METHOD 2: Linear Probing

If there is already a value stored at the given location, we go to the next available location. Linearly search for an empty slot to store `key, value` pair.

#### Example
Instead of overwriting at `index` location as in our original implementation, now we will iterate through the `linked-list` and find the correct location to update our value..

**Code:**

```python
class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]    


table = HashTable()
table['6-Mar'] = 200

print(table.arr) # Each element will be a list
# print(table['17-Mar'])
print(table['6-Mar'])

```
---
## Stack
**Last In First Out (LIFO)** data structure. An example usage can be **browser history**, where we can press the `back` button and get the last visited website. We use `push` and `pop` opeartion to insert and get items from thew stack.

### Complexity
* Push/Pop element: `O(1)`
* Search element by value: `O(n)`

### Example Uses
* **Function Calling** in any programming language is managed by using a stack
* **Undo** (Ctrl + Z) funcitionality in any editor uses a stack to track down last set of operations.

### Comparison with List/Array
In case of **list or array**, if we need to allocate additional memory, it will be costly. If we don't have enough capcaity for additional elements, it will copy all the existing elements to another location which is inefficient w.r.t both time and memory.
This is one of the reasons why it is `not recommened` to use **list** as stack in python. The recommended approach is to use **collections.deque**, which is based on **doubly linked-lists**.

---
## Queue
**Queue** is `FIFO` (First In First Out) data stucture.