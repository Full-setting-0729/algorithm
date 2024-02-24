import sys
from collections import deque
import heapq as hq

n,m,x = map(int,input().split())

go_route =[[] for _ in range(n+1)]
back_route =[[] for _ in range(n+1)]

go_cost = [[1e12]for _ in range(n+1)]
back_cost = [[1e12] for _ in range(n+1)]
res = 0

for i in range(m):
    a,b,c = map(int,input().split())
    go_route[a].append(b)
    back_route[a].append(b)
    go_cost[a][b] = back_cost[b][a] = c

    #출발->x
    que = deque()
    que.append([x,0])
    while que:
        now,cost = que.popleft()
        for nx in go_route[now]:
            