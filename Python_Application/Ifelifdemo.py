print("---------------------------------")
print("-----Tickit Prizing Software-----")
print("---------------------------------")

print("Please Enter Your Name ; ")

Age = int(input())

if (Age <= 5):
    print("Free Entry")

elif (Age > 5 & Age <=18 ):
    print("Tickit Prise : 900")

elif ( Age > 18 & Age <= 40 ):
    print("Tickit Prise : 1200")

else:
    print("Tickit prize : 500")

