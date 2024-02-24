import math

def prim():
    dab = 0
    chk[1] = 1
    for i in range(1,n):
        dis[i] = map[1][i]
        if chk[i] == 0 and min > dis[i]:
            min = dis[i]
            k = i
    for i in range(1,n-1):
        if k == -1:
            break
        dab += min
        chk[k] =1
        min = math.inf
        mink = -1
        for j in range(1,n):
            if chk[j]==0 and dis[j] > map[k][j]:
                dis[j] = map[k][j]
            if chk[j] == 0 and min > dis[j]:
                min = dis[j]
                mink = j
        k = mink

n = int(input())
m = int(input())

arr = [[0]*(n+1) for i in range(n+1)]
chk = [0]*(n+1)
dis = [0]*(n+1)

for i in range(m):
    a,b,cost = map(int,input().split())
    arr[a][b] = cost
    arr[b][a] = cost

#while(True):
#    if chk not in 0:
#        break
#    i = 1
#    chk[i] = 1
#    dis = arr[i]
#    min1 = 0
#    for j in range(2,n-1):
#        if arr[i][j] < min:
#            min1 = arr[i][j]



