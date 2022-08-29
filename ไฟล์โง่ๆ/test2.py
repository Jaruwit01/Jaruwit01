import random
s = ["Raiden","Eula"]
z =["Riktor","Aleister"]
number = random.random()
mynumber = number*100
print(mynumber)
for i in range(1,1001):
    if i==100:
        if mynumber > 0 and mynumber <= 10:
            print("Xingqui")
        elif mynumber > 10 and mynumber <= 35:
            print(random.choice(s))
        elif mynumber > 35 and mynumber <= 65:
            print(random.choice(z))
        else:
            print("Vincent")
