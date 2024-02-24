def leafnode(par):
    global cnt
    if tree[par]:
        for child in tree[par]:
            leafnode(child)
    else:
        cnt += 1



n = int(input())
arr = list(map(int,input().split()))


tree = [[] for _ in range(n)]
result = 0
delete = int(input())

root = 0

for i in range(n):
    if i == delete and arr != -1:
        continue
    elif arr[i] != -1:
        tree[arr[i]].append(i)
    else:
        root = 1
print(root)


if delete != root:
    cnt = 0
    leafnode(root)
    print(cnt)

