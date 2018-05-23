# Module Notes

# Modules are programs that can be imported into and used by other programs.
# They allow you to reuse code across multiple files more easily. The easiest
# way to create a module using Python is to write all the functions and
# variables you'd like to include into a .py file.

# Example:

# import sys module
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

# In the above example I imported the sys module without specifying a location
# because it's built into Python. When running the code above in the terminal
# type: python modules.py we are arguments

# You don't have to import an entire module if you don't want the whole thing.
# Use from to import a specific function or variable from that module.

# Example:

# import random to make this example more interesting
import random
# import the square root function from the math module
from math import sqrt

# Set num to a random number between 1 and 300
num = random.randint(1,300)

# Print out the square root of the random number. Testing my knowledge of
# strings and .format() here.
print('The square root of {} is'.format(num), sqrt(num))

# Module Naming
# Modules have names to check and see if they're being run standalone or by
# another module. Access this using __name__

# When creating your own module you can import it by saying import module_name
# in the file you want to create. All .py files are modules in that they can be
# imported to other files.

# Example:

# A hypothetical mymodule.py file:
def say_hi():
    print('Hi, this is my module speaking.')

__version__ = '0.1'

# If the above code was in a different file you'd import it to this one by
# writing:
# (this is commented out to avoid errors when running this
# file. I created this repo more for my own notes than practice. That will come
# later.)

# import mymodule
# mymodule.say_hi()
# print('Version', mymodule.__version__)
