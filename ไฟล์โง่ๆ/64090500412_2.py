char = input() #รับเป็น string
indexnum = [int(x) for x in input().split(',')] #รับเป็นแบบ int 1บรรทัด โดยใช้ , ขันระหว่าง
s = 0
for i in indexnum:
    print(char[s+i], end='')
    s +=i