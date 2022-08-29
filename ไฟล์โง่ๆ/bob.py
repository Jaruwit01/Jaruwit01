# a = input()
# b = input().split()
# n = 0
# for i in b:
#     c = i.strip(',."\'()')
#     if c == a:
#         n+=1
# print(n)


# s = []
# while True:
#     a = input()
#     s.append(a)
#     if s[0] == 'q':
#         print('No Data')
#         exit()
#     elif a == 'q':
#         s.remove('q')
#         break

# d = list(map(float, s))
# m = sum(d)/len(s)
# x = round(m, 2)
# print(x)

# import math
# a = float(input())
# b = math.log(a,10)
# d = round(b, 6)
# print(d)

# a = input()
# b = input()
# s = []
# d = []
# if len(a)>len(b):
#     print('Incomplete answer')
# else:
#     for i in a:
#         s.append(i)
#     for x in b:
#         d.append(x)
#     n = 0
#     for j in range(len(a)):
#         if s[j] == d[j]:
#             n+=1
#             j = j + 1
#     print(n)

#-------------------------------------------------------------
# import re
# a = input()
# d = '\d'
# c = re.findall(d,a)
# s = []
# num = ['0','1','2','3','4','5','6','7','8','9']
# for x in num:
#     if x not in c:
#         s.append(x)
# if len(s) > 0:
#     print(','.join(s))
# else:
#     print('None')        

#----------------------------------------------------------------------------------
# def mosteller(w, h):
#      mtl = ((w*h) **0.5) / 60
#      return mtl
     

# def du_bois(w, h):
#      db = 0.007184 * (w**0.425) * (h**0.725)
#      return db

# def fujimoto(w, h):
#      fjmt = 0.008883 * (w**0.444) * (h**0.663)
#      return fjmt

# def main():
#      weight = float(input()) 
#      height = float(input())
#      mostellers = mosteller(weight, height)
#      du_boiss = du_bois(weight, height)
#      fujimotos = fujimoto(weight, height)
#      print("Mosteller =", round(mostellers, 5))
#      print("Du Bois =", round(du_boiss, 5))
#      print("Fujimoto =", round(fujimotos, 5))
     
# exec(input())

# ------------------------------------------------------------
# x1, x2 = (int(x,2) for x in input().split())
# print(bin(x1 + x2)[2:])

# #==============================================================
# def is_prime(n):
#      if n <= 1:
#           return False
#      for k in range(2, int(n**0.5)+1):
#           if n%k == 0:
#                return False
#      return True
# def next_prime(N):
     
     
def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n % k == 0:
            return False
    return True

def next_prime(n):
    if n == 1:
        return 2
    elif n%2 == 0 :
        n += 1
    while True:
        if is_prime(int(n)) == True:
            return n
            break
        n += 2

def next_twin_prime(n):
    if n%2 == 0:
        n += 1
    while True:
        if is_prime(int(n)) == True and is_prime(int(n)+2):
            return n,n+2
            break
        n += 2

exec(input().strip())