print_kwargs = lambda **kwargs : kwargs
print(print_kwargs(a = 1, b = 2, c = 3)) # {'a': 1, 'b': 2, 'c': 3}
print(print_kwargs(a = 1, b = 2, c = 3, d = 4)) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(print_kwargs(a = 1, b = 2, c = 3, d = 4, e = 5)) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def print_kwargs(**kwargs):
    print(kwargs)
    return kwargs

print(print_kwargs(a = 1, b = 2, c = 3)) # {'a': 1, 'b': 2, 'c': 3}

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    return kwargs

print(print_kwargs(a = 1, b = 2, c = 3)) # {'a': 1, 'b': 2, 'c': 3}