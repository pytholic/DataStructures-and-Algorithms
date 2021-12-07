'''
-> Keep fastest growing term
-> Drop the constans
'''

# --------------TIME BASED-----------------------
data = ['A', 'B', 'C']
data2 = ['D', 'E', 'F']

for i in range (0, len(data)):
	print(i)

'''
length = n
=> time complexity is O(n)
=> Our algo will gro obe-to-one (linearly) with the array size
'''


for j in range (0, len(data2)):
        print(j)

'''
O(n1 + n2)
'''

for i in range (0, len(data)):
    for j in range (0, len(data2)):
        print(i + j)

'''
O(n**2)
=> nested loops
=> scales faster, bad algorithm
=> problems, slow
'''


for i in range (0, len(data)):
    for j in range (0, len(data2)):
        print(i + j)

for j in range (0, len(data2)):
        print(j)


'''
O(n**2 + n) => O(n**2)
''' 


# -------------------SPACE BASED-----------------------  
'''
=> Memory usage as input size scales
'''

data = ['A', 'B', 'C']

for i in range (0, len(data)):
    print(i)

'''
O(1) => stays constant
=> Space complexity is zero, since we are not adding any extra space
=> We are not creating anything inside of this
'''

data = ['A', 'B', 'C']
out = []

for i in range (0, len(data)):
    out[i] = data[i]

'''
O(n)
=> Output array will be of same length as our input
=> same amount of memory as input
'''

data = ['A', 'B', 'C']
out = []

for i in range (0, len(data)):
    out[i] = []
    for j in range (0, len(data)):
        out[i][j] = data[i]

'''
O(n**2)
=> output size will squared of input size
'''