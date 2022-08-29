num=8
for x in range(1,num+1): #ข้อที่ 51
    if x==1 or x==num :
        for y in range(1,num+1):
            print('*',end='')
        print()
    else:
        for y in range(1,num+1):
            if y==1 or y==num: #ข้อที่ 53
                print('*',end='')
            else:
                print('-',end='')
        print()