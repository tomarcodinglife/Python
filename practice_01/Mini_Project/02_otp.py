import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# First Method



def OtpGenerator(digit = 4):
    otp = ""
    for i in range(digit):
        otp += str(random.choice(numbers))
    print (f"OTP Generator is {otp}")





OtpGenerator(4)
OtpGenerator(5)
OtpGenerator(6)

# Second Method

myotp = (
    random.choice(numbers), 
    random.choice(numbers),
    random.choice(numbers),
    random.choice(numbers)
)

print(f"my otp is {myotp}")


