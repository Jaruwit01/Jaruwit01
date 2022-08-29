Dec = int(input())
Hex = '0123456789ABCDEF'
Hexdecimal = ''
while Dec != 0:
    Index = Dec%16
    Dec = Dec // 16
    Hexdecimal += str(Hex[Index])
a = str(Hexdecimal)
print(Hexdecimal[::-1])
