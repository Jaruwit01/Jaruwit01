# ข้อ 1
#h, m, s, = [int(x) for x in input().split()]
#print(((h*60)*60)+(m*60)+s) 

#===========================================================
# ข้อ 2
#import math

#x = int(input())
#y = 2-x + ((3/7)*(x**2)) - ((5/11)*(x**3)) + math.log(x,10)
#print(y)


#===========================================================
# ข้อ 3

#a = int(input())
#x = 1
#for i in range(4):
   # i = (x + (a/x))/2
#print(i)

#===========================================================
# ข้อ 4

#import numpy 

#v1, v2, v3 = [int(x) for x in input().split()]
#u1, u2, u3 = [int(x) for x in input().split()]
#v = [v1, v2, v3]
#u = [u1, u2, u3]
#c = numpy.dot(v,u)
#print(c)

#===========================================================
# ข้อ 5

#x1, y1, x2, y2 = [int(x) for x in input().split()]
#print((((x1 - x2)**2)+((y1 - y2)**2))**0.5)

#===========================================================
# ข้อ 6

#import math

#r, theta = [int(x) for x in input().split()]
#x = r*math.cos(theta)
#y = r*math.sin(theta)
#print(x,y,end=" ")

#===========================================================
# ข้อ 7

#import math

#x, y = [int(i) for i in input().split()]
#r = ((y**2)+(x**2))**0.5
#theta = math.atan(y/x)*180
#print(x,round(theta,2),end=" ")

#===========================================================
# ข้อ 8

#median = [int(i) for i in input().split()]
#print(sum(median)/5)

#===========================================================
# ข้อ 9

#a, b, c = input().split()
#print(a+b+c+((int(c)*(a+b))))

#===========================================================
# ข้อ 10

#import numpy
#a = [int(x) for x in input().split()] #หามัธยฐาน
#print(numpy.median(a))

#===========================================================
# ข้อ 11

# number = sorted([int(x) for x in input().split()]) 
# print(number[1])

#===========================================================
# ข้อ 12

# x1, y1, r1 = (int(x) for x in input().split())
# x2, y2, r2 = (int(x) for x in input().split())

# if (x1-x2)**2 + (y1-y2)**2  > (r1+r2)**2:
#    print('free')
   
# elif (x1-x2)**2 + (y1-y2)**2  < (r1+r2)**2:
#    print('overlap')

# elif (x1-x2)**2 + (y1-y2)**2  == (r1+r2)**2:
#    print('touch')


#===========================================================
# ข้อ 13

# x, y = (int(i) for i in input().split())
# if x > 0 and y > 0 :
#    print('อยู่ในจตุภาค 1')
# elif x < 0 and y > 0 :
#    print('อยู่ในจตุภาค 2')
# elif x < 0 and y < 0 :
#    print('อยู่ในจตุภาค 3')
# elif x > 0 and y < 0 :
#    print('อยู่ในจตุภาค 4')
# elif x == 0 and y == 0 :
#    print('อยู่จุกำเนิด')
# elif x == 0 and (y > 0 or y<0 ):
#    print('อยู่บนแกน Y')
# elif (x > 0 or x < 0 ) and y == 0:
#    print('อยู่บนแกน x')

#===========================================================
# ข้อ 14

# a = [int(x) for x in input().split()]
# if a[0] < a[1] < a[2] < a[4]:
#    print('True')
# else:
#    print('False')

#===========================================================
# ข้อ 15

# number = [int(x) for x in input('Number:').split()]
# n = sorted(number)
# print('sum:', n[1]+n[2])  

#===========================================================
# ข้อ 16

# a = int(input('a:'))
# n = 0
# while True:
#    if a != n**3:
#       n+=1
#       if a == n**3:
#          print('x:', n)
#          break
#       elif a < n**3:
#          print('Not Found')
#          break

#===========================================================
# ข้อ 17
# number = int(input('รอบอก:'))
# if number < 37:
#    print('ขนาด XS')

# elif number == 37 and number < 41:
#    print('ขนาด S')
# elif number == 41 and number < 43:
#    print('ขนาด M')
# elif number == 43 and number < 46:
#    print('ขนาด L')
# elif number > 46 :
#    print('ขนาด XL')
   
#===========================================================
# ข้อ 17

# while True:
#    k = 1
#    a = (1/k)*k
#    if (a) == 1:
#       k+=k
#    elif (a) != 1:
#       print('K:', k)
#    else:
#       print("ไม่มีคำตอบ") ลันไม่ออก

#===========================================================
