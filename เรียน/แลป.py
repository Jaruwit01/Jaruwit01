# s = input('s:').split()
# p = input('p:')
# n = 1
# j = []
# for i in s:
#     if i == p:
#         j.append(n)
#         n+=1
#     else:
#         j.append(i)
# print(*j)

#--------------------------------------------------------------
# f = []
# s = []

# for i in range(6):
#     a = tuple(int(x) for x in input().split())
#     s.append(a)
# for x in s:
#     if x not in f:
#         f.append(x)         
# print(f)

#-----------------------------------------------------------
# d = {}
# for i in range(3):
#     name, age = input().split()
#     d.update({name:age})
# name_key = input()
# print(d[name_key])



a, b = (float(x) for x in input().split())
com = complex(a, b)
con = com.conjugate()+com
con = con.real

if con.is_integer():
    print(str(con)[:-2])

else:
    print(con)   