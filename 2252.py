from collections import deque

n,m = map(int,input().split())

arr = [[] for _ in range(n+1)]
cnt = [0] * (n+1)
que = deque()
dab = []
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    cnt[b]+=1
for i in range(1,n+1):
    if cnt[i] == 0:
        que.append(i)
while que:
    tmp = que.popleft()
    dab.append(tmp)
    for i in arr[tmp]:
        cnt[i] -= 1
        if cnt[i] == 0:
            que.append(i)
print(*dab)