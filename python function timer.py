import time

def function_timer(function):
    def timer(*args):
        before = time.time()
        result = function(*args)
        after = time.time()
        print(f'Function {function.__name__} took {round(after - before,10)} seconds to run.')
        return result
    return timer
        
@function_timer
def comp():
    numbers = [i for i in range(1000)]

@function_timer
def rang():
    numbers = []
    for i in range(1000):
        numbers.append(i)
        
@function_timer
def list_func():
    numbers = list(range(1000))

comp()
rang()
list_func()