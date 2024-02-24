import sys
input = sys.stdin.readline

n,k = map(int,input().split())
graph = [[0]*n for _ in range(n)]

#그래프 작성
for i in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1


for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
s = int(input())

for _ in range(s):
    x,y = map(int,input().split())
    if graph[x-1][y-1] == 1:
        print(-1)
    elif graph[y-1][x-1] == 1:
        print(1)
    else:
        print(0)

#

