import locale
money = int(input())
if money == 0 or money < 150000 :
    print("Hurray, tax exempted")

elif money == 150001 or money < 300000 :
    a = int(((money-150000) * 0.05))
    print(f"{a:,}")

elif money == 300001 or money < 500000 :
    a = int(((money-300000) * 0.1) + (150000*0.05))
    print(f"{a:,}")

elif money == 500001 or money < 750000 :
    a = int(((money-500000) * 0.15) + (150000*0.05) + (200000*0.1))
    print(f"{a:,}")

elif money == 750001 or money < 1000000 :
    a = int(((money-750000) * 0.2) + (150000*0.05) + (200000*0.1) + (250000*0.15))
    print(f"{a:,}")

elif money == 1000001 or money < 2000000 :
    a = int(((money-1000000) * 0.25) + (150000*0.05) + (200000*0.1) + (250000*0.15) + (250000*0.2))
    print(f"{a:,}")

elif money == 2000001 or money < 5000000 :
    a = int(((money-2000000) * 0.3) + (150000*0.05) + (200000*0.1) + (250000*0.15) + (250000*0.2) + (1000000*0.25))
    print(f"{a:,}")
    
elif money >= 5000001 :
    a = int(((money) * 0.35) + (150000*0.05) + (200000*0.1) + (250000*0.15) + (250000*0.2) + (300000*0.3) +(3000000*0.3))
    print(f"{a:,}")
