a = int(input())
b = int(input())
c = int(input())
d = a+b+c
print(d)
if d>=80 and d<=100:
    print("A")
elif d>=75 and d<79:
    print("B+")
elif d>=70 and d<74:
    print("B")
elif d>=65 and d<69:
    print("C+")
elif d>=60 and d<64:
    print("C")
elif d>=55 and d<59:
    print("D+")
elif d>=50 and d<54:
    print("D")
elif d<=49:
    print("F")
else:
    print("Error")
