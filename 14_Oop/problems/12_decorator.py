import time
# it is also called function factory
def timeCalculation(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =  function(*args, **kwargs)
        end = time.time()
        print(f"{function.__name__}ran in {end - start} time")
        return result
    return wrapper


@timeCalculation
def exampleFunction(n):
    time.sleep(n)
    print(f"example function execute in in {n}") 

exampleFunction(2)

# example function execute in in 2
# exampleFunctionran in 2.0004541873931885 time
