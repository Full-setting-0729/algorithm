from collections import defaultdict

INF = 1000000000

def dfs(x):
    if x == 0:
        return
    dfs(via[x])
    dab.append(x)

def dijkstra(s):
    dis = [INF] * (N + 1)
    dis[s] = 0
    for _ in range(1, N):
        if s == -1:
            break
        chk[s] = 1
        min_val = INF
        mink = -1

        for j in range(1, N + 1):
            if chk[j] == 0 and dis[j] > dis[s] + graph[s][j]:
                dis[j] = dis[s] + graph[s][j]
                via[j] = s
            if chk[j] == 0 and min_val > dis[j]:
                min_val = dis[j]
                mink = j

        s = mink

    return dis

N = int(input())
M = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
chk = [0] * (N + 1)
via = [0] * (N + 1)
dab = []

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

x, y = map(int, input().split())

distances = dijkstra(x)
print(distances[y])

dfs(y)
print(len(dab))
print(*dab)