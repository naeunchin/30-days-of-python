# === STRINGS ===

# Any data under single, double, or triple quotes 
# Multiline string is created using triple single or triple double quotes

multiline_string_1 = '''This is a multiline string
that spans multiple lines.'''
multiline_string_2 = """This is another multiline string
that spans multiple lines."""

"""
Most common escape characters: 
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
"""

print('I say \"Hello, World!\"')

# === STRING FORMATTING ===
# There are 3 ways to format strings (oldest -> newest):  % operator, .format(), F-strings

# % operator is used to format a set of variables enclosed in a tupule (fixed size list), together with a format string, which contains normal text together with "argument specifiers", which are special symbols that map data types to output layouts.
"""
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
"""
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

# .format() method inserts parameters sequentially or via index/keywords markers into {} placeholders
print("Hello, {}. You are {}.".format("Bob", 25))
print("Hello, {1}. You are {0}.".format(25, "Bob"))
print("Hello, {name}. You are {age}.".format(name="Bob", age=25))

# F-strings: fast, clean, highly readable way to format strings by prefixing a literal string with f or F and placing variables or expressions directly inside curly braces {}
    # Introduced in Python 3.6
    # Evaluated at runtime 
    # More efficient than .format() or % formatting 

name = "Alice"
age = 30
print(f"Hello, {name}. You are {age} years old.")
# Output: Hello, Alice. You are 30 years old.

# Supports inline expressions and operations
print(f"Next year you will be {age + 1}.")
# Output: Next year you will be 31.

# === STRING CHARACTERS === 
# Python strings are sequences of chars (0-indexed) that allow access to methods that apply to objects (lists, tupules)
# Can extract single char from strings 
# negative indexing: start from right end (-1 is the last index, -2 is the second last index, etc.)

# e.g., P, y, t, h, o, n
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# Slicing strings into substrings using the slice operator (colon)
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three)   # hon
# Can skip chars by passing a step arg to slice method 
pto = language[0:6:2] 
print(pto) # Pto

# Reverse strings using the syntax [start:stop:step] where step is -1
# Leaving start and stop empty will reverse the string
reversed_language = language[::-1]
print(reversed_language) # nohtyP
# Can also use the reversed() function combined with the join() method to reverse a string
reversed_language = ''.join(reversed(language))

# === STRING METHODS ===
# Python has a set of built-in methods that can be used on strings.
# e.g., capitalize(), upper(), lower(), title(), strip(), split(), replace(), find(), index(), isalpha(), isdigit(), isspace(), join(), format(), count(), startswith(), endswith() etc.
# https://www.w3schools.com/python/python_ref_string.asp