# Function Notes

# Start functions with def. Then write an identifyier (or an name for the
# function) followed by closed parenthesis which include any parameters for the
# function (variables) and a colon. Write the code the function should execute
# indented below. Unlike Ruby, don't need to write "end" at the end of the
# function. In Python the function ends when the indentation goes down. Unlike
# JS and Ruby indentation seems to be very important for defining variables.

# Everyone's first function:

def say_hello():
    print("Hello World")

# Call the function:
# say_hello()

# Variables defined within a function cannot be called outside of it. The same
# is true for variables in classes. Python variables have both local and global scope.

# If you call a global variable in a function and change it, it only changes
# within the function. If you call the variable again outside of the function
# it's value will remain unchanged.

# Example:

x = 50

def do_thing(x):
    print('x started at', x)
    x = 20
    print('x is now', x)

do_thing(x)
print('x is once again', x)

# You can make a variable global by declaring it as "global." This way you can
# change global variables within functions.

# Example:

def do_other_thing():
    global x
    print('x started at', x)
    x = 20
    print('x is now', x)

do_other_thing()
print('Hey, x actually changed to', x)

# It's also possible to assign default values to a function's parameters. This
# helps when a user doesn't want to provide values for your input. This is done
# within the parameters when defining the function.

# Example:

# Takes a message and prints it the number of times the user inputs. If there's
# no input, print once.
def talk(message, times=1):
    print(message * times)

talk("Hello!")
talk("Hello ", 5)

# Additionally when you have several parameters for a function but only want to
# specify some of them you can do so using keywords. Write "x=4" in the
# parameter. Because you're specifying which value you want to define this can
# be done out of order within the function's parameters when its called instead
# of ordering it in the same way it was defined.

# When you don't want to have a set number of arguments you can use asterisks
# to take in any number of arguments. Single asterisk will take all arguments
# from that point until the end of the parameters as that "param." Double
# asterisks will take all keyword arguments. These are stored as tuples and
# dictionaries.

# Example:

def total(a=5, *numbers, **phonebook):
    print('a=', a)

    # Loop through all the numbers and print them out
    for i in numbers:
        print(i)

    # Loop through the phonebook
    for i, d in phonebook.items():
        print(i, d)

total(10,1,2,3,Jack=1123,John=2231,Inge=1560)

# Return statements break a function, ending it right there. All functions
# contain a return none statement at the end by default. Set this if you want
# to return something specific at the end of the function.

# Docstrings are used to document a program. They can be used while the program
# is running. Write the docstring as a string on the first line of the
# function's executable code and it can be called later by using .__doc__

# Example:

def doc_string_ex(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integers. They are evaluated to see which is bigger.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is the max')
    else:
        print(y, 'is the max')

doc_string_ex(18, 21)
print(doc_string_ex.__doc__)
