# === LISTS ===

"""
4 collection types in Python that store data in a single variable: 
- List [1, 2, 3]: ordered, indexed, mutable collection; duplicates allowed
- Tupule (1, 2, 3): ordered, indexed, immutable collection; duplicates allowed; often used for fixed, read-only data structures 
- Set {1, 2, 3}: unordered, unindexed, and immutable collection (but can add new items); duplicates not allowed (dupes are automatically eliminated)
    - Use set() to create an empty set
    - {} initializes an empty dictionary
- Dictionary {'a': 1}: unordered and indexed collection of key-value pairs; keys are immutable/hashable data types like strings, num, tupules; duplicates not allowed 
"""

# Create lists using built-in function 
list_1 = list()
# Create lists using square brackets 
list_2 = []

# len() finds the length of the list 
fruits = ['banana', 'orange', 'mango', 'lemon'] 
print('Number of fruits:', len(fruits)) # 4

# Lists can have items of different data types 
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

# Use positive indexing to access items from L (beginning) -> R
# Use negative indexing to access items from R (end) -> L (end)
vegetables = ['Tomato', 'Potato', 'Cabbage']
             # -3         -2          -1

# --- Unpacking list items ---
# Can extract values from a list into variables or other data structures 
# Useful for situations like assignments, function args, and iteration 

li = [1, 2, 3]
# Unpacking list elements into variables 
a, b, c = li    # variables a, b, c are 1, 2, 3, respectively 

# Can use the star (*) operator for unpacking 
    # Can capture multiple values in one variable 
    # Useful when we don't know the exact number of elements in the list of when we want to extract a few elements 
li = [1, 2, 3, 4, 5]
a, b, *rest = li    # variable 'rest' will be [3, 4, 5]

# Can use * in the middle 
li = [1, 2, 3, 4, 5, 6]
a, *mid, c = li     # a = 1 / mid = [2, 3, 4, 5] / c = 6

# Can unpack nested lists (lists within lists)
li = [1, [2, 3], 4]
a, (b, c), d = li   # variables a, b, c, d are 1, 2, 3, 4 respectively 
# The inner list [2, 3] is unpacked directly into the variables b and c using () 

# Slicing items from a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
orange_and_mango = fruits[1:3] # it does not include the first index
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
