# === CONDITIONALS === 
# Statements in the Python script are executed sequentially from top to bottom 
# Sequential flow of execution can be altered in 2 ways: 
    # Conditional execution: block of >=1 statements will be executed if a certain expression is true 
    # Repetitive execution: block of >=1 statements will be repetitively executed as long as a certain expression is true 

# If  
    # Check if the condition is true and execute the block code 
    # syntax is indentation after the colon (:)
a = 3
if a > 0:
    print('A is a positive number')

# If else 
    # If condition is true the first block will be executed, if not the else condition will run
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# If elif 
    # Multiple conditions 
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# Shorthand: code if condition else code 
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

# Nested conditions 
a = 0
if a > 0: 
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

# Can make code more readable by using the logical operator AND 
a = 0 
if a > 0 and a % 2 == 0: 
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive number')
elif a == 0:
    print('A is zero')
else: 
    print('A is negative')

# OR operator 
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted')
else:
    print('Access denied')

# --- EXERCISES ---
user_age = int(input('Enter your age: '))
if user_age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need {18 - user_age} more years to learn to drive.')

"""
Grade calculator:
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
"""
grade = int(input('Enter your grade: '))
if grade >= 90:
    print('Your grade is A')
elif grade >= 80:
    print('Your grade is B')
elif grade >= 70:
    print('Your grade is C')
elif grade >= 60:
    print('Your grade is D')
else:
    print('Your grade is F')

# Get a month from user input and print season 
month = input('Enter a month, capitalize the first letter: ')
if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring')
else: 
    print('The season is Summer')

fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
if 'apple' not in fruits:
    fruits.append('apple')
    print(fruits)
else: 
    print('That fruit already exists in the list')