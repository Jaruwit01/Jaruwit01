n = int(input())
s=[]
d=[]
for i in range(n):
    s.append(int(input()))
for o in s:
    if o%2 !=  0:
        d.append(o)
print(d)
