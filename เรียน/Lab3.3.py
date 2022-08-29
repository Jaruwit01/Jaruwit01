"3.2"
'''import random
output = 0
loop_count = 1
xingqui, Eula, Raiden, Aleister, Riktor, vincent = 0, 0, 0, 0, 0, 0
while True:
    check = random.random()
    if check <= 0.1:
        xingqui += 1
    elif check > 0.1 and check <= 0.35:
        avatar_check = random.random()
        if avatar_check >= 0.5:
            Eula += 1
        else:
            Raiden += 1
    elif check > 0.35 and check <= 0.65:
        avatar2 = ["Riktor", "Aleister"]
        avatar_check = random.random()
        if avatar_check >= 0.5:
            Aleister += 1
        else:
            Riktor += 1
    else:
        vincent += 1
    if loop_count % 10 == 0:
        print (loop_count)
        print("xiangqui : ", xingqui, "Raiden, Eula :",
              Raiden+Eula, "Riktor, Aleister : ", Riktor+Aleister, "vincent :", vincent)
    output = (vincent*100)/loop_count
    if output >= 34.99 and output <= 35.01:
        print(output)
        break
    loop_count += 1'''

" 3.1 "
import random

xingqui, Eula, Raiden, Aleister, Riktor, vincent = 0,0,0,0,0,0
for i in range(1,1001):
    check = random.random()
    if check <= 0.1:
        xingqui +=1
    elif check > 0.1 and check <= 0.35:
        avatar_check = random.random()
        if avatar_check >= 0.5:
            Eula += 1
        else:
            Raiden +=1
    elif check > 0.35 and check <= 0.65:
        avatar2 = ["Riktor", "Aleister"]
        avatar_check = random.random()
        if avatar_check >= 0.5:
            Aleister +=1
        else:
            Riktor +=1
    else:
        vincent += 1
    if i %100 == 0:
        print("xiangqui : ", xingqui,"Raiden, Eula :",
              Raiden+Eula, "Riktor, Aleister : ",Riktor+Aleister,"vincent :", vincent)
