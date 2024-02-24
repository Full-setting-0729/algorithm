from collections import deque

n = int(input())

mapping = [[0] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    mapping[a].append(b)
    mapping[b].append(a)

que = deque()
que.append(1)

chk = [0]*(n+1)

def bfs():
    while que:
        now = que.popleft()
        for nx in mapping[now]:
            if chk[nx] == 0:
                chk[nx] = now
                que.append(nx)
bfs()

result = chk[2:]

for x in result:
    print(x)






