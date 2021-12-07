'''
Collision: Two keys trying to store value at the same location.
So, we need to handle these collisions.
'''

'''
METHOD 1: Chaining

We can use an approach called 'chaining'. Instead of directly storing the value, we store
a linked-list or a list at every location.

This list can keep on growing and multiple keys can share the same hash value.

However, our complexity now can grow from O(1) to O(n) i.e. when we have a bad hashing 
function and all the keys generate the same index. Then all of our values will be stuck in 
one list.

In that case search complexity will be same as of a linked-list which is O(n). Because after
getting hash value, we have to linearly search through whole list.

For that reason, it is important to have our 'key' stored in each of these elements. So that
we know which value is associated with which key.
'''

'''
METHOD 2: Linear Probing

If there is already a value stored at the given location, we go to the next available location.
Linearly search for an empty slot to store key, value pair.

'''
        
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