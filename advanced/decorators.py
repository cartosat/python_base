"""
Python Decorators
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