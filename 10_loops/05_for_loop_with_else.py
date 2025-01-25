num = [1, 2, 3, 50, 100, 87]

for i in num:
    print(i)
else:
    print("done")

'''
1
2
3
50
100
87
done
'''



for i in enumerate(num):
    print(i)
else:
    print("Done")
'''
(0, 1)
(1, 2)
(2, 3)
(3, 50)
(4, 100)
(5, 87)
Done
'''