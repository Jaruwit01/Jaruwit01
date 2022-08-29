a = int(input())
b =int(a/16)
l = '0123456789ABCDEF'
while (b<a) != 0:
    d = a-(16*b)
    print(l[d])
    break