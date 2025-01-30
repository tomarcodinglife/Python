# celsius / 5 = (fahrenheit-32)/9
# celsius = 5 X (fahrenheit-32)/9

def f_to_c(f):
    print(f"{(f-32)*5/9}° Celsius")
    return((f-32)*5/9)

fahrenheit = int(input("Enter Fahrenheit Number for Convert in Cesius: "))

f_to_c(fahrenheit)
