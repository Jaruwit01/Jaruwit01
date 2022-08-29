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
while True:
        number = random.random()
        mynumber = number*100
        #print(mynumber)
        if mynumber > 0 and mynumber <= 10:
            Xingqui.append(mynumber)
            print("Xingqui")
        elif mynumber > 10 and mynumber <= 35:
            number = random.random()
            mynumber = number*100
            if mynumber >= 50:
                Raiden.append(mynumber)
            else:
                Eula.append(mynumber)
            print(random.choice(s))
        elif mynumber > 35 and mynumber <= 65:
            number = random.random()
            mynumber = number*100
            if mynumber >= 50:
                Riktor.append(mynumber)
            else:
                Aleister.append(mynumber)
            print(random.choice(z))
        else:
            Vincent.append(mynumber)
            print("Vincent")
        Test = len(Vincent)/(len(Xingqui) + len(Raiden) + len(Eula) + len(Riktor) + len(Aleister) + len(Vincent))*100
        if Test > 34.99 and Test < 35.01:
            break
        else:
            x += 1