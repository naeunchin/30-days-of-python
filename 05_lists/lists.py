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
    # -1 refers to the last item, -2 refers to the second last item
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
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2nd item - ['banana', 'mango']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']


# --- Modifying lists ---
fruits = ['banana', 'orange', 'mango', 'lemon']
# Can modify individual element in the list by accessing the index 
fruits[0] = 'avocado'
last_index = len(fruits) - 1
fruits[last_index] = 'lime' # the last element is now lime 

# Use the IN operator to check if an item is in the list 
does_exist = 'banana' in fruits # True 
does_exist = 'potato' in fruits # False

# Can use the method append() to add item to the end of an existing list
fruits.append('apple') # Will append apple to the end of the list 
# Can use the method insert() to insert a single item at a specified index in a list 
    # Other items will be shifted to the right! 
    # insert() takes 2 args: index, item for insertion 
fruits.insert(2, 'kiwi') # will insert kiwi at index 2, shifting other items to the right 

# Can use the remove() method to remove a specified item from a list 
    # Method will remove the first occurrence of the item in the list (in case there are dupes)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')

# pop() removes the specified index (or the last item if index is not specified)
fruits.pop() # Removes the last item 
fruits.pop(0) # Remove item at index 0

"""
The DEL keyword can: 
- remove the specified index
- delete items within index range
- delete the list completely
"""
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0] # Delete banana
del fruits[1:3] # Delete items between index 1 to 3 (non-inclusive) - mango, lemon
del fruits # Delete the whole list 

# clear() empties the list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear() # List is empty 

# Can copy a list by reassigning it to a new variable (list2 = list1)
    # list2 is a reference to list1 so any changes we make in list2 will also modify the original list (list1)
    # To keep the original list intact and unchanged, use the method copy() 

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits__copy = fruits.copy()

# Can join or concatenate >=2 lists using the + operator or extend() method 
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_vegetables = fruits.extend(vegetables) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# count() returns the number of times an item appears in a list 
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24)) # 3

# index() returns the index of an item in the list (or the first occurrence, in case of dupes)
print(ages.index(24)) # 2, which is the first occurrence 

# reverse() reverses the order of a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse() # ['lemon', 'mango', 'orange', 'banana']

# --- Sorting list items ---
# sort() reorders the list items in ascending order (alphabetical if string & ascending if num) and modifies the original list 
    # Can set the argument 'reverse' (bool) to True to arrange the list in descending order 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort() # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True) # reverse-alphabetical order: ['orange', 'mango', 'lemon', 'banana']

# sorted() returns the ordered list without modifying the original list 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True) # ['orange', 'mango', 'lemon', 'banana']


# EXERCISES 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )
# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method