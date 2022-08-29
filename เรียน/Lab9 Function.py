#Lap9.1
"""def triangle(nline, diff):
    for q in range(1, nline+1):
        a = diff*q - (diff-1)
        print(a*'*')

triangle(5, 2)
print("_"*30)"""


#Lap9.2
import math

def trigonometry(x):
    sin = math.sin(math.radians(x))
    cos = math.cos(math.radians(x))
    sin = str(f" {sin:.2f}").center(10)
    cos = str(round(cos,2)).center(10)
    return sin, cos

print("   มุม           sin           cos")
n=0
while n <= 360 :
    
    print(str(n).center(10),trigonometry(n))
    n+=22.5
                           

print("_"*30)



#Lap9.3
"""def rectangle(width=5, height=5):

    for i in range(height):
        for x in range(width):
            print("*", end="")
        print()
    
rectangle(6,2)
print("_"*10)"""