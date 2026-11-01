# === DICTIONARY ===

# A dictionary is a collection of unordered, mutable, indexed key-value pairs.
# Use {} or the dict() function to create a dictionary
# Value can be of any data type: bool, list, tuple, set, dict 

person = {
    'first_name':'Jane',
    'last_name':'Doe',
    'age':30,
    'country':'Canada',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

# len() can be used to check the number of key:value pairs in the dictionary 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

# Access the dictionary items using the key name inside square brackets or get() method
    # Accessing an item by key name raises an error if the key does not exist
    # Using get() method returns None (a NoneType object data type) if the key does not exist and does not raise an error 
print(person['first_name']) # Jane
print(person.get('first_name')) # Jane

# Add new key and value pairs to the dictionary using assignment operator
person['job_title'] = 'Data Scientist'
person['skills'].append('SQL') # Adding a new skill to the skills list

# Modify items in a dictionary by accessing the key and assigning a new value
person['age'] = 31 # Modifying the age value

# Check if a key exists in a dictionary using the IN operator (returns bool)
print('first_name' in person) # True
print('sex' in person) # False

# Remove items from a dictionary using the pop() method or the del keyword
    # pop(key): removes the item with the specified key name
    # popitem(): removes the last item
    # del: removes the item with the specified key name but does not return the value

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item

# items() changes the dict to a list of 2-element tuples 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# clear() clears items 
dct.clear()

#  delete() deletes the dictionary 
del dct

# copy() copies the dictionary without mutating the original dict 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# keys() gives us all the keys of a dictionary as a list 
keys = dct.keys()
print(keys) # dict_keys(['key1', 'key2', 'key3', 'key4'])

# valus() gives us all the values of a dictionary as a list 
values = dct.values()
print(values) # dict_values(['value1', 'value2', 'value3', 'value4'])
