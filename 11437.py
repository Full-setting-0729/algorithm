def dfs(x,depth):
   chk[x] = 1
   level[x] = depth

   for n in tree[x]:
       if chk[n] == 1:
           continue
       p[n] = x
       dfs(n,depth+1)

def lca(a,b):
    while level[a] != level[b]:
        if level[a] > level[b]:
            a = p[a]
        else:
            b = p[b]
    while a!=b:
        

n = int(input())

tree = [[]for _ in range(n+1)]
chk = [0]*n
level = [0]*n
p = [0]*n
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)


dfs(1,0)


print(tree)

