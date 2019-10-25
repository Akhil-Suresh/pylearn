# Decorators
# ==========
#   A decorator takes in a function, adds some functionality and returns it.
#   This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.
#   This is possible by the very base feature of python. 
#       - Functions can be passed as arguments to another function. 
#         Such function that take other function as arguments are called higher order functions.
#       - A function can return another function.

def decorator_function(func):
    def decorating_function():
        print "this will print at the start"
        func()
    return decorating_function

# You may be wondering how func is available inside decorating_function
# This happens because of LEGB pattern of variable identification
# L - Local, E - Enclosing, G - Global, B - Builtin
# so 'func' is found inside Enclosing function.


#  Another intresting thing to note here is that the decorator_function will get called only once and 
#  decorating function will get called as many times we are decorating same function with it
#  I know you didn't get a shit about what I said now. Look at the end I put an example for this

def main():
    print "This should be printted as second anyhow"

# Very Basic approach
# This is what is happening behind the scene
print "A very basic approach"
formatted_way = decorator_function(main)
formatted_way()

# A much efficient way will be
print "An efficient way"
main = decorator_function(main)
main()

# This is simplified into 
print "Following a new style"
@decorator_function
def main():
    print "This should be printed as second"

main()

# Decorating functions with parameters
# ====================================

# In the above scenario we have nothing as parameters to our
# main of function. What to do when we need to pass parametes?

def check_permission(func):
    def decorating_function(*args, **kwargs):
        print "Checking permission"
        if 'grant_permission' in args:
            print "Access granted"
            func(*args, **kwargs)
        else:
            print "Sorry you have no access"
    return decorating_function


@check_permission
def main(*args, **kwargs):
    pass

permission = 'grant_permission'
main(permission)

# Chaining Decorators
#     Multiple decorators can be chained in Python.

def print_stars(func):
    def inner(*args, **kwargs):
        count = kwargs.get('count')
        print "*" * int(count)
        func(*args, **kwargs)
        print "*" * int(count)
    return inner

def print_hash(func):
    def inner(*args, **kwargs):        
        count = kwargs.get('count', 10)
        print "#" * int(count)
        func(*args, **kwargs)
        print "#" * int(count)
    return inner

@print_hash
@print_stars
def main(*args, **kwargs):
    print "Printed inside function"

main(count=10)

# Note we cant pass default values to decorator

# Passing parameters into Decorator
# We will be curious enough to know what will happen or how will an argument could be 
# passed into a decorator
# Something similar is required when you call @decorator_function(passing_arguments)
# in real life 
# main = decorator_function(main)(passing_arguments)
# so this calls for an other function over decorator_function

def decorator_main_function(passed_in_args):    
    def decorator_function(func):       
        def inner(*args, **kwargs):
            print (args, kwargs)            
            x = func(*args, **kwargs)
            return x
        return inner
    return decorator_function

@decorator_main_function('access_granted')
def main(*args, **kwargs):
    """
        This function is starting ponit of execution 
    """
    print "This is visible"

main('test', value=1000)

print "Note that this is gonna cost a lot \n\
Doing so will rename the above main function into inner \n \
To avoid that happening you can use @wraps"
print main.__name__
print main.__doc__


#  The example for what I mentioned above
#  Imagine a requirement like we need to execute a function only once per minute. So what we gonna do?
#  We can go for assigning the current time to a global variable and subtract time from it and check and mess!
#  Or we can make use of decorator and above mentioned fact.
import time

class CallTooOftenError(Exception):
    pass

def execute_once_per_min(func):
    last_invoked = {'time' : 0}
    def inner(*args, **kwargs):        
        elapsed_time = time.time() - last_invoked['time']
        if elapsed_time < 60:
            raise CallTooOftenError("Only {elapsed_time} has passed".format(elapsed_time=elapsed_time))
        last_invoked['time'] = time.time()
        return func(*args, **kwargs)
    return inner

@execute_once_per_min
def main(msg):
    print msg

main("I am getting printed")
main("I shouldn't be getting printed")


# Class realization of Decorator
class MyDecorator(object):

    def __init__(self, func):
        print "Inside my decorator init"
        self.func = func

    def __call__(self):
        print " Inside call of function"
        self.func()

@MyDecorator
def aFuntion():
    print "inside aFunction"

print "Decorating function finished"



# Class Decorators
# Class Decorators is introduced in Python 2.6.  
# A class decorator is a function which gets a python class as an input..

def trace(kls):
    original_init = kls.__init__
    def __init__(self, *args, **kws):
        print("Instantiating an object of class {}".format(kls.__name__))
        original_init(self, *args, **kws)
    kls.__init__ = __init__
    return kls

@trace
class Foo(object):
    def __init__(self, value):
        self.value = value

foo = Foo(5)
print("The value of foo is {}".format(foo.value))