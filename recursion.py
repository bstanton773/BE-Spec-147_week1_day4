import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)


#############
# Recursion #
#############


# Call Stack
# The call stack is a memory structure that tracks active function calls in a program
# Operates on a stack (Last In First Out)

import time

def func1():
    print('func1 has started')
    func2()
    print('func1 has ended')


def func2():
    print('func2 has started')
    # time.sleep(2)
    print('func2 has ended')


func1()

line_break()

def capitalize(name):
    # Take in a name, upper case the first letter and lower case the rest of the name
    return name[0].upper() + name[1:].lower()

def full_name(first, last):
    # Takes in a first and last name, capitalizes both names, and concatenates them with a space
    return capitalize(first) + ' ' + capitalize(last) # The capitalize on first needs to finish and then the capitalize on last needs to finish and then it concatenates and returns

def greet_person(first_name, last_name, day_of_week):
    person_full_name = full_name(first_name, last_name) # The full_name function needs to finish before we move on
    print(f"Hello {person_full_name}, it sure is beautiful on this {capitalize(day_of_week)}")


greet_person('bRIaN', 'stAnTOn', 'ThURsDay')


line_break()

# Recursive functions are functions that call themselves, typically with smaller input, until they reach a base case.'
# Base Case - Determines when the recursion should stop. Without a base case, the function will call itself indefinetely.

# Factorial Function
# n! = 1 if n = 1, else n * (n-1)!

def factorial(n):
    # Base Case
    if n < 1:
        raise ValueError("Cannot find the factorial of a non-positive number")
    elif n == 1:
        print(f"factorial({n}) = 1")
        return 1
    else:
        print(f"factorial({n}) = {n} * factorial({n-1})")
        return n * factorial(n-1)
    

print(factorial(5))

line_break()

# File System - Searching for a document in a folder

file_system = [
    [
        "whiteboards",
        [
            "day1",
            "whiteboard1.py",
            "test1.py"
        ],
        [
            "day2",
            "whiteboard2.py",
            "test2.py"
        ],
    ],
    [
        "my-api",
        "requirements.txt",
        "README.md",
        [
            "app",
            "__init__.py",
            "routes.py",
            "models.py"
        ]
    ],
    "notes.py",
    [
        "personal",
        [
            "photos",
            "vacation.jpg",
            "cover.jpg"
        ],
        [
            "job_search",
            "resume.pdf",
            "cover-letter.pdf"
        ]
    ]
]


def find_document(folder, document, parent='./'):
    # Loop through the folder
    for item in folder:
        # If the item is the document for which we are searching
        if item == document:
            return parent + document
        # If the item is a folder (list)
        if isinstance(item, list):
            # Get the folder name for our parent argument
            folder_name = item[0] # Assume the first element of a list is the folder name
            # Recursively call the find_document function on this subfolder
            result = find_document(item, document, parent + folder_name + '/')
            # If the document is found in that subfolder
            if result is not None:
                # Return the result
                return result


print(find_document(file_system, 'vacation.jpg'))

line_break()
# Potential Pitfalls
# Stack Overflow + Extra Overhead

# def fac(n):
#     return n * fac(n-1)

# fac(5)

# fibonacci - 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, etc
# fib(n) = fib(n-1) + fib(n-2) if n > 1, else fib(n) = 1

def hide_the_cache():
    fib_cache = {}

    def fib(n):
        if n <= 1:
            return n
        elif n in fib_cache:
            return fib_cache[n]
        else:
            fib_number = fib(n-1) + fib(n-2)
            fib_cache[n] = fib_number
            return fib_number

    return fib

fib = hide_the_cache()


print(fib(5))
print(fib(10))
print(fib(13))
print(fib(14))


print(fib(135))

# print(fib_cache)


# def decorator(func):
#     def my_wrapper():
#         print('This is happening before the function')
#         func()
#         print('This is happening after the function')
#     return my_wrapper


# @decorator
# def say_hello():
#     print('Hello World')

# @decorator
# def say_goodbye():
#     print('Goodbye World')

# say_hello()

def fib_loop(n):
    if n <= 1:
        return n
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

print(fib_loop(100))

line_break()

# Recursion can be used for looping

def reverse_print(a_list):
    if a_list:
        print(a_list[-1])
        reverse_print(a_list[:-1])


reverse_print(['a', 'b', 'c', 'd', 'e', 'f'])


# In Class Exercise

print('''
You are working on a file management application, and your task is to implement a function that calculates the total size of all files within folder. This function should recursively traverse through the folders and sum up the sizes of all files encountered.

1. Define a Python function named **`calculate_total_folder_size`** that takes a single parameter: **`folder`** (a list representing the folder structure with file sizes).
2. Implement the recursive logic inside the **`calculate_total_folder_size`** function to traverse through the nested folders and calculate the total size of all files.
3. Use the provided file system analogy to guide your implementation.
4. Upon encountering a file (leaf node), add its size to a running total.
5. Recursively traverse through subfolders to include their files' sizes in the total.
6. Return the total size of all files in the file system structure.
''')

file_system = [
    [10, 20, 30],  # Folder 1 with files of sizes 10, 20, and 30
    [15, [25, 35]],  # Folder 2 with a file of size 15, and another folder with files of size 25, and 35
    40,  # File 1 with size 40
    [45, [55, 65]],  # Folder 3 with file of sizes 45, and another folder with file sizes 55, and 65
    70  # File 2 with size 70
]

def calculate_total_folder_size(folder):
    # Start with a size of 0
    total_size = 0
    # Look at every item in the folder
    for item in folder:
        # If the item is an integer
        if isinstance(item, int):
            # Add the integer to the title size
            total_size += item
        # If the item is a list
        elif isinstance(item, list):
            # Recursively call the calculate_total_folder_size on the subfolder
            total_size_of_subfolder = calculate_total_folder_size(item)
            # Add that subfolder's size to the total_size
            total_size += total_size_of_subfolder
    # Once we loop through all items in folder, return the total size
    return total_size

print(calculate_total_folder_size(file_system)) # Output: 410 (sum of all files)


def calculate_total_folder_size(folder):
    # Start with a size of 0
    total_size = 0
    # Look at every item in the folder
    for item in folder:
        # If the item is an integer
        if isinstance(item, list):
            # Recursively call the calculate_total_folder_size on the subfolder
            total_size_of_subfolder = calculate_total_folder_size(item)
            # Add that subfolder's size to the total_size
            total_size += total_size_of_subfolder
        else:
            # Add the integer to the title size
            total_size += item
        # If the item is a list
    # Once we loop through all items in folder, return the total size
    return total_size

def get_size(folder):
    return sum(get_size(item) if isinstance(item,list) else item for item in folder)
