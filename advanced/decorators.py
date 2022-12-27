"""
Python Decorators
- Reference : https://www.scaler.com/topics/python/python-decorators/
- A decorator in Python is a function that takes another function as an argument and
    extends its behavior without explicitly modifying it.
- With decorators we can add extra feature in existing function.
- Decorators allows us to wrap another function to extend behaviour of wrapped function
	without permanently modifying it.
- Function are first class objects in python that mean they can be passed as argument.
- We can pass function as parameter and return function as well.

"""

# this is simple function to make division.
def div(a,b):
    return a/b

# This is smart div where we will add more features.
def smart_div(func): # It is accepting another function.
    # This is another function which will accepts variables that has been passed.
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    # simply return a function.
    return inner

# assign function to some variable.
div1 = smart_div(div)

print(div1(2,4))

# We can also use @  symbol insted of assigning function to some variable.
@smart_div
def div(a,b):
    return a/b

print(div(2, 4))

# In above cases function name gets modified when we try to print it with func.__name__
# to avoid this we use wraps decorator from functools

print(div.__name__) # prints inner

from functools import wraps
def smart_div(func):
    @wraps(func)
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    # simply return a function.
    return inner

@smart_div
def div(a,b):
    return a/b

print(div.__name__) # this will print div itself.