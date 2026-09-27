import math

# === VARIABLES ===

# Variable refers to a memory address in which data is stored 
# Since Python is dymanically typed, no need to state data type for a variable 
"""
Naming conventions: 
- Start with a letter or _
- Do not start with numbers, special chars, or hyphens 
- Should be mnemonic: easily remembered and associated 
- Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    - e.g.,: firstname, firstName, first_name
- Case-sensitive
- Snake case is standard
"""
# Multiple variables can be declared in one line 
# e.g., first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# === BUILT-IN FUNCTIONS ===

# print(): takes unlimited numbers of args to print message to the screen or other output device  
# len(): returns the number of items in an object (string, list, tupule, dictionary, set, etc.), takes 1 arg 
    # e.g., print(len('Hello, World!'))
# input(): gets user input 
    # e.g., first_name = input('What is your name: ')
# type(): checks the data type of certain data/variable 
    # e.g., print(type({'name':'Asabeneh'})) --> will print dict 

# === CASTING ===

# Converting one data type to another data type
"""
str(10) converts number to string 
int('10') converts string to number 
float(10) converts int to decimal 
int(9.81) will turn it into 9
list('Python') will turn it into a list ['P', 'y', 't', 'h', 'o', 'n']
"""

# === EXERCISES ===
radius_of_circle = 30
area_of_circle = math.pi * (radius_of_circle ** 2)
circum_of_circle = 2 * math.pi * radius_of_circle

print(area_of_circle)
print(circum_of_circle)

user_radius_of_circle = input('Enter the radius: ')
user_area_of_circle = math.pi * (int(user_radius_of_circle) ** 2)
print(user_area_of_circle)