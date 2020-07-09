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

