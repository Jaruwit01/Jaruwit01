r = 10 
n = 4
s = ["period  "]
for i in range(1,r+1):
    s.append(f"{i}%      ")
print(*s)

for i in range(1,n+1):
    a = []  
    a.append(f"{i}     ")
    for x in range(1,r+1):
        d = (1+x*0.01)**i
        a.append(f"{d:.3f}   ")
    print(*a)
        

