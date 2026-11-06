from countries_data import countries

# === LOOPS ===
# while loop: executes a block of code as long as a condition is true
count = 0
while count < 5:
    print(count)
    count += 1  # increment count to avoid infinite loop
    # prints from 0 to 4
else:
    print(count)

# break: used exit the loop
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break # the loop stops printing at count 3

# continue: used to skip the current iteration and continue with the next 
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue # only prints 0, 1, 2 and 4 (skips 3)
    print(count)
    count = count + 1

# for loop: iterates over a sequence (like a list, tuple, dictionary, set, string)
# Example 1: list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: 
    # number is temporary name to refer to the list's items, valid only inside this loop
    print(number) # the numbers will be printed line by line, from 0 to 5

# Example 2: string 
language = 'python'
for letter in language:
    print(letter)

# less cleaner version 
for i in range(len(language)):
    print(language[i])

# Example 3: tuple 
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# Example 4: dictionary 
person = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age' : 20,
    'country' : 'England',
    'patronus' : 'stag',
    'courses' : ['potions', 'charms', 'defence against the dark arts', 'herbology']
}

for key in person: 
    print(key)

# dict.items() returns a view object containing the dictionary's key-value pairs as tuples 
for key, value in person.items():
    print(key, value) 

# Example 5: set  
tech_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in tech_companies:
    print(company)

# range() returns an immutable sequence of numbers
    # Most commonly used to control the execution count of a FOR loop 
    # Creates a lazy iterable (i.e., calculates numbers on the fly to conserve memory instead of storing the entire sequence in RAM)
    # Syntax with args: range(start, stop, step) 
        # start (optional; default = 0): starting int of the sequence
        # stop (required): int where the sequence ends; exclusive and never included in the output 
        # step (optional; default = 1): the amount to increase / decrease each number 

lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

st = set(range(1, 11)) # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2)) # increment by 2
print(lst) # [0, 2, 4, 6, 8, 10]

# backward from start to end 
lst = list(range(11, 0 , -2))
print(lst) # [11,9,7,5,3,1]

for number in range(11):
    print(number) # prints 0 to 10 

# Nested FOR loop
"""
--- SYNTAX ---
for x in y:
    for t in x:
        print(t)
"""

for key in person:
    if key == 'courses':
        for course in person['courses']:
            print(course)

# for...else: execute the else block only if the loop completes the iterations naturally without encountering a break statement 
for number in range(11):
    print(number)
else:
    print('The loop stops at ', number)

# PASS keyword: a null operation that acts as a placeholder 
    # Nothing happens when it executes 
    # Prevents IdentationError or SyntaxError if you leave a required code block completely empty 
for number in range(5):
    pass

# === EXERCISES === 

# 1. Make a triangle of #
for i in range(1, 8): # loop runs 7 times with i going from 1 to 7, increments by 1 by default
    print('#' * i) # Each loop repeats the # character i times so each row is 1 char longer than the row before it

# 2. make a square of #
    # 8 #'s horizontally and vertically 
for i in range(8): # outer loop that runs 8 times; one row 
    for j in range(8): # runs 8 times and runs in full on every pass of the outer loop... each of its passes prints one # in the current row 
        print('#', end=" ") # print() adds a newline at the end/next output, so end=" " replaces the newline with a space
    print() # outputs only a newline, which ends the row; runs once per row, after the inner loop has printed all 8 #s

print('---')

# Alternative (not using a nested loop)
for i in range(8):
    print('# ' * 8)

# 3. print multiplication (0 * 0 = 0, 1 * 1 = 1, 2 * 2 = 4,...)
for i in range(0, 11, 1):
    print(f'{i} x {i} = {i * i}')

# 4. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items
python_tools = ['Python', 'Numpy','Pandas','Django', 'Flask']
for python_tool in python_tools:
    print(python_tool)

# 5. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 101):
    if i % 2 != 0:
        print(f'{i}')

# 6. Use the FOR loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds 
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print(f'The sum of all even numbers: {sum_evens}')
print(f'The sum of all odd numbers: {sum_odds}')

# 7. From the fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop
fruits = ['banana', 'orange', 'mango', 'lemon']

# 8. From the fruit list, loop through the list and extract all the fruits containing the word 'an'
sub_fruits = []

for fruit in fruits: 
    if ('an' in fruit):
        sub_fruits.append(fruit)
print(sub_fruits)

# 9. From the countries_data.py file, answer the questions: 
    # --- What are the total number of languages in the data ---
num_of_languages = set()

for country in countries: 
    for language in country['languages']:
        num_of_languages.add(language)
print(len(num_of_languages))

    # --- Find the ten most spoken languages from the data ---
counts = {} # In an empty dict, put the count in each pair; python sorts pairs by their first item, so no key needed 
    # keys = language names, values = counts of each language in the data
for country in countries: 
    for language in country['languages']:
        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1
 
pairs = [] # preparing the data for sorting
for language, count in counts.items(): # counts.items(): returns a dynamic view object containing the key-value pairs of a dictionary as a list of tuples 
    pairs.append((count, language)) # create a tuple where the count comes first and the language name comes second, and add it to a list called pairs 
        # In python, it sorts a list of tuples by the first element of each tuple by default 
        # by putting count first, Python will automatically sort the languages by frequency from lowest to highest 

# The pairs look like (91, 'English'), so sorting them sorts by the count. reverse=True puts the largest first (descending order), and [:10] keeps the top ten.
pairs.sort(reverse=True)

for count, language in pairs[:10]: # get the top 10 
    print(f'{language}: {count}')

    # alternative: sort the names by their count: counts.get returns the count for each language name
        # top_ten = sorted(counts, key=counts.get, reverse=True)[:10]

    # --- Find the 10 most populated countries in the world ---
        # Since there is a population key-value directly attached, can pull the data into a list 
        # sort countries from highest to lowest (descending order): list.sort()
        # can use pairs trick to put the numeric value first, then get top 10

pairs = []
for country in countries:
    population = country['population']
    name = country['name']
    pairs.append((population, name)) # create a tuple where the population comes first and the country name comes second, and add it to a list called pairs

pairs.sort(reverse=True)
for population, country in pairs[:10]:
    print(f'{country}: {population}')