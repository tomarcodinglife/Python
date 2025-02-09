# celsius / 5 = (fahrenheit-32)/9
# celsius = 5 X (fahrenheit-32)/9

def f_to_c(f):
    print(round((f-32)*5/9), 2) # round(value, Number of decimal)
    return((f-32)*5/9)

fahrenheit = int(input("Enter Fahrenheit Number for Convert in Cesius: "))

f_to_c(fahrenheit) # change

