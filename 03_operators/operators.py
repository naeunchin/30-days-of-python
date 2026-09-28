import math
# === ASSIGNMENT OPERATORS ===

# = is the standard assignment operator that assigns values to variables 
# Shorthand assignment operators perform different operations to assign the result back to the variable in a single step

# ==========================================
# BASIC ASSIGNMENT OPERATORS
# ==========================================
# =    Assignment               x = 5       ->  x = 5
# +=   Addition Assignment      x += 3      ->  x = x + 3
# -=   Subtraction Assignment   x -= 3      ->  x = x - 3
# *=   Multiplication Assign    x *= 3      ->  x = x * 3
# /=   Division Assignment      x /= 3      ->  x = x / 3 (always returns a float)
# //=  Floor Division Assign    x //= 3     ->  x = x // 3
# %=   Modulus Assignment       x %= 3      ->  x = x % 3 (returns remainder)
# **=  Exponentiation Assign    x **= 3     ->  x = x ** 3

# Bitwise operators work by converting ints into their binary format (0 = False, 1 = True) and performing logical operations on each corresponding pair of bits 
    # e.g., 5 is stored as 0101 in 4-bit binary
    # Align two numbers bit-by-bit and evaluate them from right to left
    # & (AND) = both A and B must be 1 
    # | (OR) = Either A and B must be 1 
    # ^ (XOR) = Exactly one of A and B must be 1  
# Shift operators slide the binary digits to L or R, padding the empty slots with 0s 
    # Left shift (<<) shifts bits to the L, multiplying by 2 ^ (shift amount)
        # e.g., 12 << 2 will yield 48, since 1100 shifted left by 2 positions becomes 110000 (which is 48)
    # Right shift (>>) shifts bits to the right, discarding digits that fall off the end. Floor division by 2 ^ (shift amount)
        # e.g., 12 >> 2 will yield 3, since 1100 shifted right by 2 positions becomes 0011 (which is 3)

# ==========================================
# BITWISE ASSIGNMENT OPERATORS
# ==========================================
# &=   Bitwise AND Assignment   x &= 3      ->  x = x & 3
# |=   Bitwise OR Assignment    x |= 3      ->  x = x | 3
# ^=   Bitwise XOR Assignment   x ^= 3      ->  x = x ^ 3
# >>=  Right Shift Assignment   x >>= 3     ->  x = x >> 3
# <<=  Left Shift Assignment    x <<= 3     ->  x = x << 3

print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False

# Comparison operators compare two values to check if a value is greater, less, or equal to other vaule (==, !=, >, <, >=, <=)
# Python uses keywords as comparators: 
    # is: Returns true if both variables are the same object(x is y)
    # is not: Returns true if both variables are not the same object(x is not y)
    # in: Returns True if the queried list contains a certain item(x in y)
    # not in: Returns True if the queried list doesn't have a certain item(x not in y)

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Logical operators and, or, not in Python combine conditional statements 
    # and: returns True if both statements are true 
    # or: returns True if one of the statements is true 
    # not: reverses the result, returns False if the result is true

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# == EXERCISES ===
age = 32 # 1
height = 167.9 # 2
complex_num = 3 + 4j # 3 (Complex is written in the form of a + bj, where $a$ is the real part and $b$ is the imaginary part)

base = float(input('Enter the base: ')) # need to convert to float or int because input() always returns a string 
height = float(input ('Enter the height: '))
area = 0.5 * base * height 
print('The area of the triangle is ' + str(area)) # Only strings allowed in concatenation
print(f'The area of the triangle is {area}') # Alternative

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
    # std slope-intercept formula: y = mx + b
        # m = slope, b = y-intercept 
    # Comparing y = 2x - 2 to y = mx + b, slope must be 2 
    # y-intercept is pt where x = 0 // y = 2(0) - 2 = -2 (coordinate point of (0, -2))
    # x-intercept is pt where y = 0 // 0 = 2x - 2 // x = 1 (coordinate point of (1, 0))
m = 2
b = -2
slope = m
y_intercept = (0, b) # y = b
x_intercept = (-b / m, 0) # 0 = mx + b --> x = -b / m

print(f"Slope: {slope}")
print(f"x-intercept: {x_intercept}")
print(f"y-intercept: {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)

euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len('python') != len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 'I hope this course is not full of jargon.' Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon.')

# There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'on' not in 'python')

# Find the length of the text python and convert the value to float and convert it to string
text_length = len('python')
float_length = float(text_length)
string_length = str(float_length)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print((7 // 3) == int(2.7))

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input('Enter hours: ')
rate_per_hour = input('Enter rate per hour: ')
pay = int(hours) * int(rate_per_hour)
print('Your weekly earning is ', pay)