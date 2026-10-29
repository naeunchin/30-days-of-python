# === TUPLES ===

# A collection of different data types 
    # Ordered, immutable (so cannot use modifying methods like insert, add, remove, etc.)
    # Written with () 
# Tuple methods: 
    # tuple(): creates an empty tuple
    # count(): counts the number of a specified item in a tuple
    # index(): finds the index of a specified item in a tuple
# + operator joins >= tuples to create a new one 

empty_tuple = ()
empty_tuple = tuple()
fruits = ('banana', 'orange', 'mango', 'lemon')
print(len(fruits))

# Use positive or negative indexing to access elements 
second_fruit = fruits[1]
last_fruit = fruits[len(fruits) - 1] # Use the last index or fruits[-1]
first_fruit = fruits[-4] 

# Slicing tuples
    # Specify a start and end index (end index is non-inclusive)
    # Creates a subtuple
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
all_items = tpl[-4:]         # all items (in normal order, not reversed)
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

# Change tuples to lists (or vice versa)
    # Useful to change to a list since tuples are immutable: If we want to modify a tuple, change to a list first! 
    # Convert into a new variable, original will be unchanged
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl) # tpl is changed to a list and stored in a new variable. Original tpl is unchanged
print(type(lst)) # list
new_tpl = tuple(lst) # lst is changed to a tuple and stored in a new variable
print(type(new_tpl)) # tuple

# IN operator returns a bool, whether an item exists or not in a tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment

# + operator joins >=2 tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

# Cannot remove a single item in a tuple, but can delete the tuple itself using DEL 
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits