max_ = 10
number =  5
for d in range(1,max_+1):
    if d >= number :
        print("\nMultiplication table of ",d)
        for a in range(1,6):
            mul = a*d
            print(mul,end=" ")
    else:
        print("\nMultiplication table of ",d)
        for a in range(1,11):
            mul = a*d
            print(mul,end=" ")
