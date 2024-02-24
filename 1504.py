n,m = map(int,input().split())

graph = [[0 for _ in range(n+1)]for _ in range(n+1)]
chk = [0] * n
via = [0] * n
dis = [0] * n
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = graph[b][a] = c

d,f = map(int,input().split())

for i in range(1,m):
    chk[i] = 1
    mini = min(graph[i])
    dis[i+1] += mini
    if chk[i] != 1:


print(graph)