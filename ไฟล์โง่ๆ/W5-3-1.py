import random
Xingqui = []
Raiden = []
Eula = []
Riktor = []
Aleister = []
Vincent = []
s = ["Raiden", "Eula"]
z = ["Riktor", "Aleister"]
x = 0
roll = 10000
while x < roll:
    number = random.random()
    mynumber = number*100
    #print(mynumber)
    if mynumber > 0 and mynumber <= 10:
        Xingqui.append(mynumber)
    #    print("Xingqui")
    elif mynumber > 10 and mynumber <= 35:
        number = random.random()
        mynumber = number*100
        if mynumber >= 50:
            Raiden.append(mynumber)
        else:
            Eula.append(mynumber)
    #    print(random.choice(s))
    elif mynumber > 35 and mynumber <= 65:
        number = random.random()
        mynumber = number*100
        if mynumber >= 50:
            Riktor.append(mynumber)
        else:
            Aleister.append(mynumber)
    #    print(random.choice(z))
    else:
        Vincent.append(mynumber)
    #    print("Vincent")
    x += 1
print(len(Xingqui)+len(Raiden)+len(Eula)+len(Riktor)+len(Aleister)+len(Vincent))
print("Xingqui  ",len(Xingqui)/roll*100," %")
print("Raiden   ",len(Raiden)/roll*100," %")
print("Eula     ",len(Eula)/roll*100," %")
print("Riktor   ",len(Riktor)/roll*100," %")
print("Aleister ",len(Aleister)/roll*100," %")
print("Vincent  ",len(Vincent)/roll*100," %")