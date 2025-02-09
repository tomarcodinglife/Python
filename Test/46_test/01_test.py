
def generateTabel(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open (f"C:/Users/PC/OneDrive/Documents/Python/Test/46_test/table/table{n}.txt", "w") as file:
        file.write(table)
    

for i in range (2, 5):
    generateTabel(i)