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
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27

