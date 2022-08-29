# a = input()
# s = ''
# for i in a:
#     if i == '[':
#         i = '('
#         s+=i       
#     elif i == '(':
#         i = '['
#         s+=i
        
#     elif i == ')':
#         i = ']'
#         s+=i
        
#     elif i == ']':
#         i = ')'
#         s+=i
#     else:
#         s+=i
# print(s,end='')

# a = input()
# n = 0
# m = 0
# for x  in a:
#     for i in range(len(a)):
#         if a[i] == '(' and a[i+1] ==')':
            
#             if x == '(':
#                 n+=1
#             if x == ')':
#                 m+=1
#         i = i+1
# if n == m:
#     print('pass')
# else:
#     print('fail')
  
  
# a = input()
# for i in a:   
#     if i == 'x' or i =='X':
#         pass 
#     elif i.isupper():
#         i = i.lower()
#     elif i.islower():
#         i = i.upper()
#     print(i,end='')  

# import math
# n = int(input())
# a = math.sqrt(2*math.pi() * (n**(n+(1/(2*(math.e**))))))


a = input()
for i in a:
    a = ord(i)
    b = chr(a)
    print(a, end='')
    