# === LISTS ===

"""
4 collection types in Python: 
- List: ordered and mutable collection, duplicates allowed 
- Tupule: ordered and immutable collection, duplicates allowed 
- Set: unordered, unindexed, and immutable collection (but can add new items), duplicates not allowed 
- Dictionary: unordered, indexed, mutable collection, duplicates not allowed 
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
