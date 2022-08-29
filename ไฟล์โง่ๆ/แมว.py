#1
# a = input()
# x = ['abba', 'babana', 'ann']
# n = 0
# z = []
# while n < len(x):
#     c = 0
#     for i in x[n]:
#         if a in i:
#             c+=1
#     n+=1
#     z.append(c)
# print(z)


#2
# x = [1, -4, 2, 0 , -3,]
# n = 0
# while n < len(x):
#     if x[n] < 0:
#         x.remove(x[n])
#         n+=1
#     n+=1
# print(x)


#3
# x = [1, -4, 2, 0 , -3]
# n = 0
# for i in x:
#     n+= i
# print(n)


#4
# a = [int(x) for x in input().split()]
# n = 0
# for i in a:
#     if i < 0:
#         n+=1
# print(n)


#5
# a = input()
# z = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
# s = []
# for i in a:
#     for x in z:
#         if i == x.lower() or i == x.upper():
#             s.append(i)
#         else:
#             pass
# print(''.join(s))


#6
# x = [int(c) for c in input().split()]
# y = [int(a) for a in input().split()]
# z = []
# for i in range(len(x)):
#     n = 0
#     n+=i
#     z.append(x[n] + y[n])
# print(z)


#7
# m = [[1,2,3],[4,5,6]]
# a = []
# for i in m:
#     for x in i:
#         a.append(x)
# print(a)


#8
# x = [int(a) for a in input().split()]
# x = sorted(x)
# z = []
# for i in x:
#     if i not in z:
#         z.append(i)
# print(z)


#9

# n = int(input())
# x = [j for i in range(2, n//2) for j in range(i*2, n, i)]
# x = set(x)
# print(sorted(x))


#10

# n = int(input())
# s = []
# z = []
# for i in range(2, n//2):
#     for j in range(i*2, n, i):
#         s.append(j)
# a = list(set(s))
# for t in range(2, n-1):
#     if t not in a:
#         z.append(t)
# print(a)
# print(z)


#101 2
# x =  int(input())
# s = []
# for i in range(x):
#     if i%2 == 0:
#         s.append(i)
# print(tuple(s))


#101 3
# a = int(input())
# s = []
# for i in str(a):
#     s.append(int(i))
# print(tuple(s))


#101 4
# x = input()
# s = []
# d = {}
# for i in x:
#     s.append(i)
# o = list(set(s))
# for j in o:
#     n = 0 
#     for q in s:
#         if j == q:
#             n+=1
#     d.update({j:n})

# print(d)


#101 5
# x = input()
# y = input()
# s = []
# z = []
# for i in x:
#     s.append(i)
# s = set(s)
# for j in y:
#     z.append(j)
# z = set(z)
# d = []
# for q in s:
#     for t in z:
#         if q == t:
#             d.append(q)
# print(set(d))


#101 6
# a = int(input())
# s = {}
# for i in range(a):
#     w = input().split() 
#     s.update({w[0]:w[1]})
# b = input().split()
# for q in b:
# 	for j in s:
# 		if q == s.get(j):
# 			print(j, end=" ")


#94
# def reverse(d):
#     x = list(d.items())
#     s = {}
#     for i in x:
#         s.update({i[1]:i[0]})
#     return s
# def keys(d, v):
#     x = list(d.items())
#     s = []
#     for i in x:
#         if i[1] == v:
#             s.append(i[0])
#     return s

# exec(input().strip())


# 95
# n = int(input())
# d = {}

# for i in range(n):
#     name, nickname = input().split()
#     d[name] = nickname
#     d[nickname] = name

# n = int(input())
# lst = []

# for i in range(n):
#     check = input()
#     if check in d:
#         lst.append(d[check])
#         continue
#     lst.append("Not found")

# for i in lst:
#     print(i)
    
    
# #96
# m = {}
# x = input()

# for i in range(len(x)):
#     if x[i] in m:
#         m[x[i]] = m[x[i]] + 1
#         continue
#     m[x[i]] = 1

# d2 = {}

# for i in m:
#     if m[i] in d2:
#         d2[m[i]] += (i,)
#         continue
#     d2[m[i]] = (i,)

# lst_count = [i for i in d2]
# lst_count = sorted(lst_count, reverse = True)

# for i in lst_count:
#     sort_d2i = sorted(d2[i])
#     for j in sort_d2i:
#         print(j, "->", i)
        
# #97
# p_icecream = {}

# n = int(input())

# for i in range(n):
#     name, price = input().split()
#     p_icecream[name] = price

# n = int(input())

# sale = {}

# sum = 0

# for i in range(n):
#     name, value = input().split()
#     if name in p_icecream:
#         sum += int(value) * int(p_icecream[name])
#         if name in sale:
#             sale[name] += int(value) * int(p_icecream[name])  
#         else:
#             sale[name] = int(value) * int(p_icecream[name])


# if len(sale) == 0:
#     print("No ice cream sales")

# else:
#     ans = []
#     mn = -1
#     for i in sale:
#         if mn < sale[i]:
#             mn = sale[i]
#             ans = []
#             ans.append(i)
#         elif mn == sale[i]:
#             ans.append(i)
#     ans = sorted(ans)
#     print("Total ice cream sales:", sum)
#     print("Top sales: ", end = '')
#     for i in range(len(ans) - 1):
#         print(ans[i], end = ', ')
#     print(ans[len(ans) - 1])
   
# import tkinter as tk
# def square(x):
#     n = 1
#     for i in range(x):
#         n*=2
#     return n
# sq = square()
# window = tk.Tk()
# fram = tk.Frame(window, bd=10, height=300, width=300).pack()
# label = tk.Label(fram, text="Enter the number of rows").pack()
# en = tk.Entry(fram, width=10).pack()
# label2 = tk.Label(fram, textvariable = str()).pack()
# box = tk.Button(fram, text="Click me", command=square).pack()
# window.title("Square")

# window.mainloop()

# print(2^0)

# li = [0.2, -1000, 1000, 33.21, -101.12, 0.01, 212, 0.4, -0.3, -100]
# a = list(((lambda i : 10000+i if i <0.5 and i > -0.5 else i) (i) for i in li))
# print(*a)



# a=[['k' ,[1,2,3]],['j',[-1,-2,-3,-4]],['m',[]]]
# d = {}
# for i in a:
#     if len(i[1]) == 0:
#         pass
#     else:
#         d.update({i[0]:i[1]})
# print(d)


# a = input()
# bit = [256, 128, 64, 32, 16, 8, 4, 2, 1]
# s = []
# for i in a:
#     s.append((i))
    
# for j in s[::-1]:
#     for x in bit[::-1]:
#         if j == '1':
#             print(j, end = ' ')
#         else:
#             pass
    
    
a =([1,2,3,4])
for i in range(len(a)):
    print(a[i])
    # for j in range(len(i)):
    #     print(a[i][j],end='')
    # print()