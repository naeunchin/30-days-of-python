# === FUNCTIONS ===
# A reusable block of code or statements that perform a certain task 
# Declare using the DEF keyword 
# A function is executed if called or invoked 
# Can be declared without parameters 

# Functions that do not return a value returns NONE by default 
def generate_full_name():
    first_name = 'Lucy'
    last_name = 'Chin'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name() # calling a function 

# Functions can return values (of any data type) using the RETURN statement 
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

# Functions can pass different data types as parameters 
    # If a function takes params, they are called arguments 
def square_number(x):
    return x * x
print(square_number(2))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N' # the value has to be converted to string 
    return weight 
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81)) # 100 and 9.81 are args 

def is_even (n):
    if n % 2 == 0:
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# If we pass the args with key and value (i.e., specify which arg represents which param), the order of the args does not matter 
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter 

# Can pass default values to params when we invoke the function 
    # if no arg is passed when calling the function, the default value will be used 
def greetings (name = 'User'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings()) # Will print out 'User, welcome to Python for Everyone!'

# In case we do not know the number of args we can pass to the function, can create a function which can take arbitrary number of args by adding * before the param name 
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2, 3, 5)) # 10

# Default and arbitrary number of params in functions 
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Alice','Brook','Caleb','Dylan')

# Can call a function which has named args using a dictionary with matching key names 
    # Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

    # Call the function using keyword arguments
greet(name="Alice", location="New York") # Output: Hi there Alice how is the weather in New York

    # Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

    # Call the function using dictionary unpacking
        # The ** operator unpacks the dictionary, passing its key-value pairs as keyword arguments to the function.
greet(**my_dict)  # Output: Hi there Alice how is the weather in New York    

# Can define a function to accept an arbitrary number of named args 
    # Avoid unless required, as this makes it harder to understand what the function accepts and does 
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)

# Can pass functions around as params 
def square_number(n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27

# === EXERCISES === 

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(celcius):
    farenheit = (celcius * 9/5) + 32
    return farenheit

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) != int and type(num) != float:
            return 'Provide numbers only.'
        else:
            total += num
    return total

print(add_all_nums(1, 2, 3)) # 6


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    reversed_array = []
    # use range(start, stop, step) to iterate through the array from end --> start 
    # range stop value is -1, because it is exclusive (make sure 0 is included) 
    for index in range(len(array) - 1, -1, -1):
        reversed_array.append(array[index])

    return reversed_array

print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) # ["C", "B", "A"]

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    factorial_num = 0
    if type(num) != int or num < 0:
        return 'Provide whole numbers only.'
    if num == 0 or num == 1:
        factorial_num = 1
    else:
        factorial_num = num * factorial(num - 1)
    return factorial_num

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if param:
        return False
    return True

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation)
def calculate_mean(numbers):
    if len(numbers) == 0:
        return 'List is empty.'
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    if len(numbers) == 0:
        return 'List is empty.'
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    if len(numbers) == 0:
        return 'List is empty.'
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes

def calculate_range(numbers):
    if len(numbers) == 0:
        return 'List is empty.'
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    if len(numbers) == 0:
        return 'List is empty.'
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std(numbers):
    if len(numbers) == 0:
        return 'List is empty.'
    variance = calculate_variance(numbers)
    return variance ** 0.5

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values
def show_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny

# Write a function called is_prime, which checks if a number is prime
    # Prime number is a number that is only divisible by 1 and itself (2 factors). A prime number is greater than 1.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Write a functions which checks if all items are unique in the list
def are_all_unique(lst):
    return len(lst) == len(set(lst))

# Write a function which checks if all the items of the list are of the same data type
def are_all_same_type(lst):
    if len(lst) == 0:
        return True
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True