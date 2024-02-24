from queue import PriorityQueue

n,m = map(int,input().split())

arr = [[]for _ in range(n+1)]
cnt = [0] * (n+1)
que = PriorityQueue()
dab = []
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    cnt[b] += 1
for i in range(1, n+1):
    if cnt[i] == 0:
        que.put(i)
while que:
    tmp = que.get()
    dab.append(tmp)
    for i in arr[tmp]:
        cnt[i] -= 1
        if cnt[i] == 0:
            que.put(i)
print(dab)