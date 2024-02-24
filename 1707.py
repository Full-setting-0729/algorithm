def dfs(x, y):
    global sw
    if sw == 1:
        return

    chk[x] = y
    for i in G[x]:
        if chk[G[x][i]] == -1:
            dfs(G[x][i], 1 - y)
        elif chk[G[x][i]] == y:
            sw = 1

k = int(input())

for _ in range(k):
    n, m = map(int, input().split())
    sw = 0
    chk = [-1] * (n + 1)
    G = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        G[b].append(a)
        G[a].append(b)

    for i in range(1, n + 1):
        if chk[i] == -1:
            dfs(i, 1)
        if sw == 1:
            break

    if sw:
        print("NO")
    else:
        print("YES")