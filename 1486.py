
INF = int(1e19)

n,m,t,d = map(int,input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        a = input()
        if a >= 'A' and a <= 'Z':
            graph[i][j] = a -65

