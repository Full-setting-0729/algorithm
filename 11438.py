max_dep = 100000
log = 21

n = int(input())

arr = [[]for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
tree = [[0]*log for _ in range(n+1)]

visit = [1]
level = [-1 for _ in range(n+1)]
level[1] = 0

while visit:
    now = visit.pop()

    for nx in arr[now]:
        if level[nx] != - 1:
            continue
        level[nx] = level[now] + 1
        tree[nx][0] = now
        visit.append(nx)


for i in range(1,log):
    for j in range(1,n+1):
        tree[j][i] = tree[tree[j][i - 1]][i - 1]

m = int(input())

for _ in range(m):
    a,b = map(int,input().split())

    if level[a] < level[b]:
        a,b = b,a
        for i in range(log-1,-1,-1):
            if level[a] - level[b] >= 2 ** i:
                a = tree[a][i]
        if a == b:
            print(a)
            continue

        for i in range(log-1,-1,-1):
            if tree[a][i] != tree[b][i]:
                a = tree[a][i]
                b = tree[b][i]
        print(tree[a][0])
