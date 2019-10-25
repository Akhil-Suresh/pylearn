# Partial Functions
# Partial functions allow one to derive 
# a function with x parameters to a function with fewer parameters and 
# fixed values set for the more limited function. The FUNCTOOLS module is for higher-order functions
# Functools module is for higher-order functions where functions can either act or return on other functions.

# Lets say a scenario
# Suppose you have a base function that gives power of any two values. 
# But while writing along the code you found that there is a need for 
# finding square too often so what we do we can make an other function 
# name find_square. Hmm client is happy with it. As we goes on suddenly
# we come to a realisation that like square we also need cubes as well
# now we are forced to write an other function named find_cube
# or we can make use of partial functions here 

from functools import partial
from functools import wraps


def power(x, y):
	return x ** y

power(2, 2)

find_square = partial(power,2)
find_cube = partial(power, 3)

print find_square(3)
print find_cube(2)


def decorator_function(function, argument):
    # magic sauce to lift the name and doc of the function
    @wraps(function)
    def ret_fun(*args, **kwargs):
        #do stuff here, for eg.
        print ("decorator arg is %s" % str(argument))
        return fun(*args, **kwargs)
    return ret_fun

decorator_main_function = partial(decorator_function, argument=arg)

@decorator_main('access_granted')
def main(*args, **kwargs):
    pass

main('car')