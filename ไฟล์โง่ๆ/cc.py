# a = input()
# s = []
# for i in a:
#     if i.isupper():
#         s.append("-")
        
#     elif i.islower():
#         s.append("_")
        
#     else:
#         s.append("*")
# d = ''
# for x in s:
#     print(d.join(x), end="")



a, b = (int(x) for x in input().split())
print(str(a*b)+str(a+b)+str(a-b))