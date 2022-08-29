a = int(input("Enter Number (1-3):"))
number = int(input("Enter Number to Append in List :"))
k = [2, 5, 9, 1, 4]
if a == 1:
    for i in k:

        print(i,end=" ")
elif a == 2:
    k.append(number)
    print("after append", number, "list :", k)

elif a == 3:
    if number in k:
        k.remove(number) 
        print("affter remove", number,"list", k)
    else:  
        print(number, "is not in list")
    
else:
    print("Error")
    


