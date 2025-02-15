
def debug(function):
    def wrapper(*args, **kwargs):
        print(f"args = {args}") # ('Sujit Tomar', 'Welcome to Dashboard')
        argsValue = ', '.join(str(arg) for arg in args)
        kwargsValue=', '.join(f"{key}, {value}" for key, value in kwargs.items())
        print(f"Function Name = {function.__name__}  with argsValue = {argsValue} and kwargsValue = {kwargsValue}")
        return function(*args, **kwargs)
    return wrapper


@debug
def greet(name, greeting = "Welcome to Back"):
    print(f"{greeting} - {name}")

username = "Sujit Tomar"    
greet(username, "Welcome to Dashboard")

