# #Leb10.1
# def sum_is_even(a, b):

#     for i in range(a, b): #วนลูป i ใน  a - b
#         m = 0
#         c = str(i) #แปลงค่า i เป็น สตริง
#         for x in c: #วนลูป ป ใน c เพื่อแยกแต่ละหลัก
#             m = m+int(x) #ใช้ตัวแปร m เข้ามาเก็บค่า m + ค่าแต่ละหลัก เพื่อหาผลรวม
#         if m%2 == 0: #เอาผลรวมที่หาได้มาเช็คเลขคู่
#             print(i,end=",")
       
#     print()
# sum_is_even(5,20)
# sum_is_even(95,110)
# sum_is_even(990,1010)
        

#lab10.2
def calc(a):
    s = 1
    b = a.split() #แยกข้อความโดยใช้ sprit
    c = float(b[0]) #ให้ตัวแปล c เก็บค่า b ตำแหน่งที่ 0 เป็นทศนิยม
    while s < len(b): #เงื่อนไขการวนรูป คือ s น้อยกว่า จำนวนที่นับได้ใน b
        if b[s] == "+" : #เงื่อนไขในการหาเคเรื่องหมาย
            c = c+float(b[s+1]) #ให้ c + float b ตำแห่งที่ s + 1 หรืก็คือบวกตำแน่งถัดไป
        elif b[s] == "-" :
            c = c-float(b[s+1]) 
        elif b[s] == "*" :
            c = c*float(b[s+1]) 
        elif b[s] == "/" :
            c = c/float(b[s+1]) 
        s+=2 #ครับเงือนไข่แล้ว ให้ ขยับถับไป2ตำแหน่ง
    print(c)
    
calc(" 0.16666666666666666 - 0.001388888888888889 / 2 ")

