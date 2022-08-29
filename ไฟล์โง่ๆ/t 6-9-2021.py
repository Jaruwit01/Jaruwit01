'''m = 10
g = 5
for i in range(1,m+1): 
    print("\n แม่", i)
    for d in range(1,11):
        a = i*d 
        print(a, end=" ")'''
import random
a = random.random()
print(a)
a=a*100
if a > 0 and a <= 25:
    print("Red BAll")
elif a > 25 and a <= 30:
    print("Blue BAll")
elif a > 30 and a <= 39:
    print("Black BAll")    
elif a > 39 and a <= 65:
    s ="Green Ball","Pink Ball"
    print(random.choice(s))    
elif a > 39 and a <= 65:
    s = ["Yellow Ball","Gray Ball"]
    print(random.choice(s))  
else :
    print("Glod Ball")
   

