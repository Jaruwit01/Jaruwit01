# from thai_sentiment import get_sentiment

# a = input()
# c = get_sentiment(a)
# print(c)

# a = int(input('จำนวนน้ำประปา/หน่วย: '))
# b = 26
# print(a*b)

def is_odd(n):
    if n%2 == 0 :
        return False
    else:
        return True

def has_odds(x):
    n = 0
    for i in x:
        if x[n]%2 == 0:
            n+=1
            if n >= len(x):
                return False
            else:
                pass
        else:
            return True
        
def all_odds(x):
    n = 0
    for i in x:
        if x[n]%2 != 0:
            n+=1
            if n >= len(x):
                return True
            else:
                pass
        else:
            return False
        
def no_odds(x):
    n = 0
    for i in x:
        if x[n]%2 == 0:
            n+=1
            if n >= len(x):
                return True
            else:
                pass
        else:
            return False
        
def get_odds(x):
    return [i for i in x if i%2 != 0]

def zip_odds(a,b):
    s = []
    n = 0
    for i,j in zip(a, b):
        if a[n]%2 != 0:
            s.append(a)
        elif b[n]%2 !=0:
            s.append(b)
            n+=1
    return s
    
exec(input().strip())
    