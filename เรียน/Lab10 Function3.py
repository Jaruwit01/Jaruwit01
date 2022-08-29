##Lab10.3.1
a = 'm723788237u8yh'
s = []
z = []

for i in a:
    if i.isdigit():
        i = int(i)
        s.append(i)
    
c = sorted(s)
for x in range(1, len(c)):
    if c[x] == c[x-1]:
        z.append(c[x])
        break
print(*z)
if z == []:
    print('None')

#Lab10.3.2
# def check(a = ''):
#     s = []
#     z = []
#     if a == '':
#         return ''

#     for i in a:
#         if i.isdigit():
#             s.append(i)
            
#     c = sorted(s)
#     for x in range(1, len(c)):
#         if c[x] == c[x-1]:
#             z.append(c[x])
#             return z

#     if z == []:
#         return ['None']

# ret = check('begy982u495834')
# if ret == '' :
#     print("Invalid parameter")
# else:
#     print(*ret)

