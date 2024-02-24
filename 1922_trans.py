import math

def prim():
    global dab
    chk = [0] * (N + 1)
    dis = [float('inf')] * (N + 1)
    min_val = float('inf')
    k = -1
    chk[1] = 1

    for i in range(1, N + 1):
        dis[i] = adj[1][i]
        if chk[i] == 0 and min_val > dis[i]:
            min_val = dis[i]
            k = i

    for i in range(1, N):
        if k == -1:
            break
        dab += min_val
        chk[k] = 1
        min_val = float('inf')
        mink = -1

        for j in range(1, N + 1):
            if chk[j] == 0 and dis[j] > adj[k][j]:
                dis[j] = adj[k][j]

            if chk[j] == 0 and min_val > dis[j]:
                min_val = dis[j]
                mink = j

        k = mink

    return dab  # dab 반환

N = int(input())
M = int(input())
adj = [[math.inf] * (N + 1) for _ in range(N + 1)]
dab = 0

for i in range(1, N + 1):
    adj[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = c
    adj[b][a] = c

result = prim()
print(result)