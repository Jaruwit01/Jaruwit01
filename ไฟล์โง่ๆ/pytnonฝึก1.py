# def intiger():
#     number1 = int(input())
#     number2 = int(input())
#     a = number1*number2
#     if a >1000:
#         b = number1 + number2
#         return b

#     else:
#         return a

# sum_s = intiger()
# print("Tthe result is",sum_s)

# --------------------------------------------------------------------------

# def Number_range():
#     a = int(input())
#     n = 0
#     for i in range(a):
#         n=i-1
#         if n < 0:
#             n=0
#         print( "Current Number", i, "Previous Number", n,"Sum:",n+i)

# Number_range()

# #--------------------------------------------------------------------------


# def number():
#     number1 = int(input())
#     number2 = int(input())
#     a = number1*number2
#     if a >1000:
#         b = number1 + number2
#         print("Tthe result is",b)
#     else:
#         print("Tthe result is",a)

# number()


# --------------------------------------------------------------------------

# def char():
#     a = input()
#     d = len(a)
#     for i in range(d):
#         if i%2 == 0:
#             print(a[i])
# char()

# --------------------------------------------------------------------------

# import turtle

# x = turtle.Turtle()
# def square(angle):

#     x.forward(100)
#     x.right(angle)
#     x.forward(100)
#     x.right(angle)
#     x.forward(100)
#     x.right(angle)
#     x.forward(100)
#     x.right(angle+15)

# for i in range(24):
#     square(90)

# turtle.done()


# Leb10.1
# def sum_is_even(a, b):
#     r = []
#     for q in range(a, b):
#         q = str(q)
#         d =len(q)
#         s = []
#         for i in range(d):
#             s.append(q[i])
#             if len(s) < len(str(b)):
#                 x = int(s[0])

#             else:
#                 x = int(s[0]) + int(s[i])

#         if x%2 == 0:
#             print(*s,end=" , ")


# sum_is_even(990,1010)

# lab10.2
# def calc(a):
#     s = 1
#     b = a.split() #แยกข้อความโดยใช้ sprit
#     c = float(b[0]) #ให้ตัวแปล c เก็บค่า b ตำแหน่งที่ 0 เป็นทศนิยม

#     for s in range(len(b)): #เงื่อนไขการวนรูป คือ s น้อยกว่า จำนวนที่นับได้ใน b
#         if b[s] == "+" : #เงื่อนไขในการหาเคเรื่องหมาย
#             c = c+float(b[s+1]) #ให้ c + float b ตำแห่งที่ s + 1 หรืก็คือบวกตำแน่งถัดไป
#         elif b[s] == "-" :
#             c = c-float(b[s+1])
#         elif b[s] == "*" :
#             c = c*float(b[s+1])
#         elif b[s] == "/" :
#             c = c/float(b[s+1])
#         s+=2 #ครับเงือนไข่แล้ว ให้ ขยับถับไป2ตำแหน่ง
#     print(f"{c:.2f}")

# calc(" 50 / 2 - 23.11 ")

# def List_number():
#     numbers_x = [10, 20, 30, 40, 10]
#     numbers_y = [75, 65, 35, 75, 30]

#     print("Given list:", numbers_x)
#     if numbers_x[0] == numbers_x[-1]:
#         print('result is True')

#     else:
#         print('result is False')

#     print("Given list:", numbers_y)

#     if numbers_y[0] == numbers_y[-1]:
#         print('result is True')

#     else:
#         print('result is False')

# List_number()


# def chack_str():

#     str_x = "Emma is good developer. Emma is a writer"
#     str_x = str_x.split()
#     n = 0
#     for i in str_x:
#         if i == "Emma":
#             n+=1
#     print("Emma appeared", n, "times")

# chack_str()


# def piramit():
#     n = 0
#     while n <= 5:
#         for i in range(n):
#             i = i+1
#             print(n,end="")
#         n = n+1
#         print()


# piramit()


# def Palindrom():

#     a = input("original number ")
#     c = a[::-1]
#     if a == c :
#         print("Yes. given number is palindrome number")
#     else:
#         print("No. given number is not palindrome number")

# Palindrom()


# def Result_list():

#     list1 = [10, 20, 25, 30, 35]
#     list2 = [40, 45, 60, 75, 90]
#     result = []
#     for i in list1:
#         if i%2 != 0 :
#             result.append(i)
#     for x in list2:
#         if x%2 == 0 :
#             result.append(x)
#     print("result list:", result)

# Result_list()


# def num_reverse():

#     a = input()
#     a = a[::-1]
#     for i in a:
#         print(i, end=" ")

# num_reverse()


# def Multiplication():

#     n = 1
#     while n <= 10:

#         for i in range(1,11):
#             i = i*n
#             print(i, end=" ")
#         n = n+1
#         print()

# Multiplication()

# def mypi(n):
#     sum_num = 3
#     num = 2
#     s = []
#     for i in range(n):
#         z = []
#         for i in range(num, num+3):
#             z.append(i)

#         sum_all = (4/(z[0]*z[1]*z[2]))
#         s.append(sum_all)
#         num = num+2
#     for i in range(len(s)):
#         if i%2 == 0:
#             sum_num = sum_num+s[i]
#         else:
#             sum_num = sum_num-s[i]
#     return sum_num
# for j in range(1,31):
#     print(j, mypi(j))

# def mypi(n):
#     s = []
#     sum_num = []
#     cout = 2
#     for i in range(n):
#         s.append(cout)
#         cout += 1
#         print(s)
#         if len(s) == 3:
#             sum_num.append(4/(s[0]*s[1]*s[2]))
#             cout = s[2]
#             s.clear()
#     return sum_num

# for i in range(1,6):
#     print(i, mypi(i))
# x = [3, 4, 5, 7]
# def showlist(j,num):
#     z = []
#     for i in j:
#         if num == 0:
#             if i%2 == 0:
#                 z.append(i)

#         elif num == 1:
#             if i%2 != 0:
#                 z.append(i)
#         elif num == 2:
#             z.append(i)
#     return z

# print('data 1 =', *showlist(x,0))
# print('data in list =', *showlist(x,1))
# print('data in list =', *showlist(x,2))

# k = [3, 4, 5, 7]
# q = [1, 4, 6, 3]
# def showlist():
#     my = []
#     for i in k:
#         m = 0
#         m = m+i 
#         if m%2 == 0:
#             my.append(m)
            
#     im = []          
#     for i in q:
#         n = 0
#         n = m+i 
#         if n%2 == 0:
#             im.append(n)
         
#     if len(my) > len(im):
#         return 'len(my) > len(im)'== len(my)
    
#     if len(my) < len(im):
#         return 'len(my) < len(im)', len(im)

# print(showlist())