a = int(input())
b = int(input())
c = b-a
s = [1000,500,100,50,20,10,5,2,1,0.5,0.25,0.1]
for i in s:
    if c>=i:
        print("{} บาท = {}".format(i ,int(c/i)))
        c = c % i
