import time

def chache(function):
    cacheValue = {}
    print(cacheValue)
    def wrapper(*args):
        if args in cacheValue:
            print(cacheValue)
            return cacheValue[args]
        result = function(*args)
        cacheValue[args] = result
        print(cacheValue)
        return result   
    return wrapper

@chache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
# print(long_running_function(5, 3))
# print(long_running_function(4, 3))