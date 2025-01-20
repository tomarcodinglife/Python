# Conditional Test


amountRam = int(input("Enter Amount Ram: "))
amountShyam = int(input("Enter Amount Shayam: "))
amountRohit = int(input("Enter Amount Rohit: "))
amountRahul = int(input("Enter Amount Rahul: "))
amountSuman = int(input("Enter Amount Suman: "))

if(amountRam > amountShyam and amountRam > amountRohit and amountRam > amountRahul and amountRam > amountSuman):
    print("Ram is Greater then others with amount", amountRam)
elif(amountShyam > amountRam and amountShyam > amountRohit and amountShyam > amountRahul and amountShyam > amountSuman):
    print("Shyam is Greater then others with amount", amountShyam)
elif(amountRohit > amountRam and amountRohit > amountShyam and amountRohit > amountRahul and amountRohit > amountSuman):
    print("Rohit is Greater then others with amount", amountRohit)
elif(amountRahul > amountRam and amountRahul > amountShyam and amountRahul > amountRohit and amountRahul > amountSuman):
    print("Rahul is Greater then others with amount", amountRahul)
elif(amountSuman > amountRam and amountSuman > amountShyam and amountSuman > amountRohit and amountSuman > amountRahul):
    print("Suman is Greater then others with amount", amountSuman)