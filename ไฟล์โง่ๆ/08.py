x, y = map(int, input().split())
m_1,m_2 =[],[] 
 
for i in range(x):
     m_1.append([int(j) for j in input().split()])
for i in range(x): 
    m_2.append([int(j) for j in input().split()]) 
for i in range(x):
    for j in range(y):
        print(m_1[i][j]+m_2[i][j],end=' ')
    print()