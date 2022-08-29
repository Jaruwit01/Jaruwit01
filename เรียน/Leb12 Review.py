#Leb12.1
# def mypi(n = 5):
    
#     pi = 3
#     mul = 2
#     z = []
    
#     for x in range(n):
#         s = []
#         for i in range(mul,mul+3):
#             s.append(i)
#         sum_mul = 1
#         for i in s:
#             sum_mul = sum_mul*i
#         sum_all = (4/sum_mul)
#         z.append(sum_all)
#         mul = mul+2
# #         print(s)
# #     print(z)
# # mypi()
#     for i in range(len(z)):
        
#         if i%2 == 0:
#             pi = pi+z[i]           
#         else:
#             pi = pi-z[i]
            
#     return pi

# for x in range(1,31):
#     print(x, mypi(x))


#Leb12.2
# def queue():

#     import random
#     s = []

#     while len(s) != 10:
#         ran = random.randint(0,9)
#         if ran not in s :
#             s.append(ran)

#     while True:
#         print(s)
#         chat = int(input())
#         if chat >= 0:
#             s.remove(chat)
#             s.insert(0,chat)
#         else:
#             break
    
# queue()    
    
        