# === SETS ===

# Set is a collection of unordered, unique, un-indexed elements 
    # Used to store unique items 
    # Does not have indices!
    # Can find the union, intersection, difference, symmetric difference, subset, super set, and disjoint set among sets

# set() function creates an empty set 
st = set()
# Initializing with elements inside {} creates a set with items
    # An empty {} creates a dictionary, which is different from a set
    # A set stores unique, standalone elements {item} whereas a dictionary stores data as key-value pairs {key:value}
st = {'item1', 'item2', 'item3', 'item4'}

# len() finds the length of a set 
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits)) # 4

# Use loops to access items in a set (iteration; loop through all items)
    # Cannot access items in a set using the index or key 
    # Since sets are unordered, the items will be processed in an unpredictable sequence (i.e., printed in any order)
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Membership testing: Check items in a set using the IN operator (returns a bool)
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("banana" not in thisset)

# add() adds one item to a set 
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

# update() allows you to add multiple items to a set 
    # takes a list arg
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

# remove() removes an item from a set 
    # If the item is not found, remove() will raise errors... check if the item exists in the given set first! 
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

# discard() can also remove an item and will not raise errors if the item is not found 
st.discard('item2') # Safe, no error raised 

# pop() removes a random item from a set and returns the removed item 
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

# clear() empties a set
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

# del operator deletes the set 
st = {'item1', 'item2', 'item3', 'item4'}
del st

# Can covert a set to list, and vice versa. Coverting the list to a set will remove duplicates from the list and only unique items will be reserved
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

# Can join two sets using the union() method or the | operator
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# Alternative: print(fruits | vegetables)

# update() method can also be used to join two sets, but it will modify the original set
    # Inserts a set into a given set 
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# intersection() returns a set of items which are in both the sets or using the & symbol
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# Alternative: st1 & st2

# A set can be a subset (set where all its elements are contained within another set) or superset (set that contains all the elements of another set)
    # issubset() and issuperset() methods return bools to check if a set is a subset or superset of another set
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

# Difference returns elements only found in the first set; elements in A that are not in B 
    # Operator syntax: A - B
python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.difference(dragon)     # {'p', 'y', 't'} - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python

# symmetric_difference () method returns a set that contains all items from both set, but not the items that are present in both sets; elements in A or B, but not both 
    # Operator syntax: A ^ B
python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'} - excluding o and n, as they are shared
# python ^ dragon

# Disjoint sets are sets that have no elements in common; returns True if two sets have a null intersection
    # isdisjoint() method returns a bool to check if two sets are disjoint

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item    

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}

# --- EXERCISES ---

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print(len(age)) # 8
print(len(age_set)) # 5 (excludes duplicates)

# "I am a teacher and I love to inspire and teach people." How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split() # using a string built-in method to split the sentence into a list of words
unique_words = set(words)
print(len(unique_words)) # 10 (unique words in the sentence)
