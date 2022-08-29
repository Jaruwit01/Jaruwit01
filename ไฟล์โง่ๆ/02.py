pi = 0
k = 1
m = 1
while k<400000:
    pi =pi+m*(1/k)
    m = -m
    k+=2
print("pi = ", pi*4 )
