'''
if n = 3
   *
  ***   
 *****
'''

n = int(input("Enter Num: "))

for i in range (1, n + 1):
    print(" " * (n-i), end="") 
    # print(f"n = {n}, i = {i} and n-1 = {n-i}")
    print("*" * (2*i-1), end="")
    # print(f"i = {i} and 2*i-1 = {2*i-1}")
    print(" ")
