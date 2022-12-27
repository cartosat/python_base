# Q: Does Python have a switch-case statement?

# We do not have a switch-case statement till python 3.9
# Python 3.10 has something called `match` which provides a
#   first-class implementation of a "switch" for Python.

def switch(ele):
    match ele:
        case 1:
            return 'One'
        case 2:
            return 'Two'
        case 3:
            return 'Three'


print(switch(1))