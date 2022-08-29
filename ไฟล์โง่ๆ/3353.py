def prisum():
    
    wide,long,high= (int(x) for x in input().split())
    area = wide*long
    volume = area*high

    return volume

prisume = prisum()
print("ปริมาตรของปริซึ่ม  = ",prisume," ลูกบาศก์")


def cylindrical():

    import math

    high ,r = (int(x) for x in input().split())
    volume = math.pi*(r**2)*high
    b = round(volume,2)

    return b

cylindricale = cylindrical()
print("ปริมาตรของทรงกรบอก  = ",cylindricale," ลูกบาศก์  ")


def conical():

    import math

    hight,rs = (int(x) for x in input().split())
    volume = math.pi*(rs**2)*hight*(1/3)
    a = round(volume,2)

    return a

conicale = conical()
print("ปริมาตรของทรงกรวย  = ",conicale," ลูกบาศก์  ")


def round_shape():
    
    import math

    r = int(input())
    volume = math.pi * (r**3) * (3/4)
    a = round(volume,2)

    return a
round_shapes =round_shape()
print("ปริมาตรของทรงกลม = ",round_shapes," ลูกบาศก์  ")



