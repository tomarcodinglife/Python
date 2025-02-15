import time

def example_Function(n):
    start = time.time()
    time.sleep(n)
    end = time.time()
    print("example function execute") # it is execute after 2 second
    print(f"{example_Function.__name__} ran in {end - start} time")

example_Function(2)
# example function execute
# example_Function ran in 2.0001413822174072 time