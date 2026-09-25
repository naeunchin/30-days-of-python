# === PYTHON BASICS ===

# COMMENTS 
"""
Multi-line comment
"""

# OPERATORS

"""
Addition + 
Subtraction - 
Multiplication *
Division /
Modulus %
Exponentiation ** (3 ** 2 = 3 * 3 = 9)
Floor division: removing remainder // (3 // 2 = 1)
"""

def add_three(num1, num2, num3):
    sum_three = num1 + num2 + num3
    print(sum_three)

add_three(1, 2, 3)

# DATA TYPES

# Python is dynamically typed: no need to explicitly declare variable types 
# Data types are automatically determined at runtime 
# type(x) tells you the data type of certain data or variable 

"""
Text Type: str (single, double, or triple quotes)
Numeric Types: int, float (decimal point or exponential notation, like 2.51 or -0.001), complex (Numbers with a real and imaginary part, written with a j or J (e.g., 2+3j))
Sequence Types:	list (ordered, mutable, can be of varying data types), tuple (immutable collection, parentheses, e.g., (1, 2, 3)), range (used for looping)
Mapping Type: dict (key-value pairs, in {}, mutable)
Set Types: set (unordered collection of unique elements, curly braces, mutable, e.g., {1,2,3}), frozenset (immutable version of set)
Boolean Type: bool
Binary Types (handles raw binary data like images, files, machine code, network packets): bytes (single bytes, ints 0-255, immutable), bytearray (ordered, mutable), memoryview (allows access to internal data of the object without making a copy)
None Type: NoneType (represents the absence of a value or a null value, like None, often used as placeholder or a function return value)
"""

print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple