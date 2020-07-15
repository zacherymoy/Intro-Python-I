'''Hello World'''
#print("Hello World")

'''bignum'''
# exp1 = 2**65536
# print("The exponent of 2**65536 = ",exp1)

'''data types'''

# x = 5
# y = 7
# sum = x + y

# print("x + y =", sum)

# x1 = 50
# y2 = 7
# sum1 = x1 + y2

# print("x1 + y2 =", sum1)

'''modules'''



"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os

# print(sys.argv)
# print(sys.platform)
# print(sys.base_exec_prefix)
# print(os.getpid())
# print(os.getcwd())
# print(os.getlogin())

'''04_printing'''

# x = 10 
# y = 2.25 
# z = "I like turtles!"

# formatter = "x is {}, y is {}, z is {}"

# print(formatter.format(x, y, z))

# print(f"x is {x}, y is {y}, z is {z}")

'''05_lists shaky on this'''

# x = [1, 2, 3]
# y = [8, 9, 10]

# # Change x so that it is [1, 2, 3, 4]
# x.append(4)
# x

# # Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# # YOUR CODE HERE
# x = x + y
# x

# # Not sure 
# # Change x so that it is [1, 2, 3, 4, 9, 10]

# # x.remove(8)
# # print(x)

# # x.pop(8)
# # x

# # Change x so that it is [1, 2, 3, 4, 9, 99, 10]

# x.insert(5, 99)
# print(x)

# # Print the length of list x

# print(len(x))

# # Print all the values in x multiplied by 1000

# print([i * 1000 for i in x])

"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use
parens instead of square brackets.

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values
never needs to be mutated, use a tuple instead of a list.

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically.
"""

# Example:

import math

def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b

    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))



# Write a function `print_tuple` that prints all the values in a tuple

# YOUR CODE HERE

# t = (1, 2, 5, 7, 99)
# print_tuple(t)  # Prints 1 2 5 7 99, one per line

# # Declare a tuple of 1 element then print it
# u = (1)  # What needs to be added to make this work?
# print_tuple(u)

"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 
This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295
Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[4])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
print(a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:6])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[0:5])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[6:12])

"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 
Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [1, 2, 3, 4, 5]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squared = [number ** 3 for number in y1]
print("Values squared:\n", squared)

print(y1)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]
lst = [a.upper() for a in a]
print(lst) 

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

#x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
str1 = input("Please Enter your Own String : ")

str2 = ''
i = 1
while(i <= len(str1)):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
    i = i + 1
        
print("Original String :  ", str1)
print("Final String :     ", str2)

"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).
The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
waypoints.append({'lat':20,'lon':100,'name':'somewhere else'})

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

waypoints[0]['name'] = 'not a real place'
waypoints[0]['lon'] = -130

# Write a loop that prints out all the field values for all the waypoints
for way in waypoints:
    print(way)

# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard

# Print out "Even!" if the number is even. Otherwise print "Odd"
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

def f1(arg1, arg2):
    return arg1 + arg2

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"

# WOW

def f2(*args):
    # print(type(args[0]))
    return sum(args)

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
print(f2(*a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.
def f3(n1, n2=1):
    return n1 + n2


print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# Initialy work 
# def f4(a, b):
#   print(f"key: a, value: {a} key: b, value:{b}")

def f4(**kwargs):
    for key, val in kwargs.items():
        print(f'key: {key}, value: {val}')

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
f4(**d)

# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.

x = 12

def change_x():
    global x
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".


    print(y)


outer()

"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# Do you bite your thumb at us, sir?
# I do bite my thumb, sir.
# Do you bite your thumb at us, sir?
# No, sir. I do not bite my thumb at you, sir, but I bite my thumb, sir.
# Do you quarrel, sir?
# Quarrel, sir? No, sir.


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

import sys
import calendar
from datetime import datetime
from datetime import date

# ask of month and year
year = int(input("Please Enter the year Number: "))
month = int(input("Please Enter the month Number: "))

# Displaying the Python calendar
print(calendar.month(year, month))