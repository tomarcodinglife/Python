print("--------------------Break---------------------------")
for i in range(10):
    if(i == 8):
        break # exit loop right now
    print(i)


'''
--------------------Break---------------------------
0
1
2
3
4
5
6
7
'''


print("---------------------Continue----------------------")
for i in range(10):
    if(i == 5):
        continue # Skip this iteration
    print(i)

'''
---------------------Continue----------------------
0
1
2
3
4
6
7
8
9
'''