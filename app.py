import math


# ***********************************
# ****** SECTION 1 - FUNCTIONS ******
# ***********************************

# A function is some block of code that can be called upon to run when you need it.
# You will also hear me use the term "METHOD". For now you can assume
#   these are synonyms (although in Python there is a difference)
# A function has the following syntax
# def function_name():
#   Contents of the function are tabbed in just like an if statement or a loop


def make_dog_noises():
    print("bark")
    print("woof")
    print("grrrr")


def make_cat_noises():
    print("meow")
    print("hiss")
    print("prrr")


# A function does nothing until is has been called
# To call a function you say its name and add parenthesis

# make_dog_noises()
# make_cat_noises()

# NOTE: You can only call on a function once it exists. Try calling this method before line 13.

# ******************************************
# ****** SECTION 2 - INPUT PARAMETERS ******
# ******************************************

# A function can accept and number of input parameters as needed
# They go inside of the parenthesis when a function is defined
def add_numbers(first_number, second_number):
    print(first_number + second_number)


# When you call on a function with input parameters you have to supply the requested arguments.
# add_numbers() # This will cause an error because it is expecting 2 arguments but we didn't provide them.
# add_numbers(first_number=3, second_number=5)
# NOTE: you are not required to specify the name of the parameter. You can just pass them in order.
#   But specifying the name makes your code easier to read.


# A parameter can have default value if you want. Set it equal to something when it is defined.
def print_location(city, state, postcode, country="USA"):
    print(f"{city}, {state}, {postcode}, {country}")


# print_location(city="Cincinnati", state="Ohio", postcode="45328")
# print_location(city="Calgary", state="Alberta", postcode="T0L 2A0", country="Canada")


# You can pass in an arbitrary dictionary of parameters.
# Put ** before the list of arguments. It is common to use the shorthand args but you can call it whatever you want.
def print_arbitrary_location(**args):
    print(f'{args["city"]}, {args["state"]}, {args["postcode"]}, {args["country"]}')


# print_arbitrary_location(city="Jackson", state="Wyoming", postcode="83001", country="USA")


# ***************************************
# ****** SECTION 3 - RETURN VALUES ******
# ***************************************

# A function can send a value back to the code wherever it was called.
# We use the keyword "return" and specify which value is sent.
# A return statement stops a function from running.

def quadratic_equation(a, b, c, is_addition):
    result = math.sqrt(math.pow(b, 2) - (4 * a * c))
    if not is_addition:
        result = result * -1
    result = (-1 * b) + result
    result = result / (2 * a)
    return result


# Notice that the function call becomes a number when the value returns.
first_root = quadratic_equation(1, 2, -8, True)
second_root = quadratic_equation(1, 2, -8, False)

# print(f"The roots of the equation are {first_root} and {second_root}.")

# *******************************
# ****** SECTION 4 - SCOPE ******
# *******************************

# Any variable or object created inside of function only exists inside of that function
# The scope of a variable/object is the area of the code where it exists

x = 2
def ugly_test():
    y = 3
    print(f"Inside the function y is {y}.")
    print(f"Inside the function x is {x}.")
    # x = 7
    # print(f"Inside the function x was changed to {x}.")

# ugly_test()
# print(f"Outside the function x is still {x}")
# print(f"Outside the function y does not exits. Lets cause an error {y}.)

# **********************************
# ****** SECTION 5 - DRY CODE ******
# **********************************

# DRY stands for "Done Repeat Yourself"
# DRY code is good code
# If you find yourself writing the same code more than once it is a good idea to make a function instead.
