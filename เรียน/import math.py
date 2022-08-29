import math
#x = 1
#f = (math.pi*x)-(3/x)+(7*(x**5))-(math.log(x,10))-(math.e**(-x))
#print(f)
#R = float(input("input the radius of circles = "))
#Carea = math.pi*(R**2)
#print(round(Carea , 5))
a,b,c,=[int(x) for x in input().split()] 
x = ((-b)+((b**2)-(4*a*c))**0.5)/(2*a)
x2 = ((-b)-((b**2)-(4*a*c))**0.5)/(2*a)
if (b**2)-(4*a*c) == 0:
    print(x)
elif (b**2)-(4*a*c) > 0: 
    print(x,x2,end="")
elif (b**2)-(4*a*c)<0:
    print("No Solution in real number.")
