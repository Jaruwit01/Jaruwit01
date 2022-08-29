# import numpy as np

# def get_column_from_bottom_to_top(A, c):

#     a = A[:, c]

#     return a[::-1]


# def get_odd_rows(A):

#     return A[1::2, :]


# def get_even_column_last_row(A):

#     return A[-1,0::2]


# def get_diagonal1(A):
#     s = []

#     n = 0

#     for i in A:
#         s.append(i[n])

#         n+=1

#     return np.array(s)


# def get_diagonal2(A):
#     s = []

#     n = 2

#     for i in A:
#         s.append(i[n])

#         n-=1

#     return np.array(s)

# exec(input().strip())

#________________________________________________________________________________________________



# import numpy as np


# def toCelsius(f):

#     f = np.array(f)

#     return (f - 32) * 5 / 9


# def BMI(wh):

#     wh = np.array(wh)

#     return (wh[:,0] / (wh[:,1]**2))*10000



# exec(input().strip())


#________________________________________________________________________________________________


# def reverse(d):

#     d = dict(d)
#     s =[]

#     for v,k in d.items():

#         s.append(k)

#         s.append(v)

#     return dict(zip(s[::2],s[1::2]))


# def keys(d, v):

#     d = dict(d)
#     s =[]

#     for k,d in d.items():

#         if d == v:

#             s.append(k)
#     return s

# exec(input().strip())

#________________________________________________________________________________________________

# n = int(input())
# s = []

# for i in range(n):

#     s.append(input().split())

# k = []
# for i in s:

#     name = {i[x]:i[x+1] for x in range(0,len(i),2)}

#     k.append(name)


# # z = []
# # for i in s:

# #     for j in i:

# #         z.append(j)

# # name = {z[i]:z[i+1] for i in range(0,len(z),2)}


# m = int(input())

# g = []

# for i in range(m):

#     b = input()

#     g.append(b)

# for d in g:

#     for i in k:

#         if d in i.keys():

#             print(*i.values())

#         elif d in i.values():

#             print(*i.keys())

#         # else: print('Not found')
        

m,n = (int(x) for x in input().split())
s = []
for i in range(m):

    z = []

    for j in range(n):
        a = input()
        z.append(a)     
    s.append(z)
print(s)


