def dfs(x,y):
    if x == n-1 and y == m-1 :
        return arr[x][y]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if arr[nx][ny] < arr[x][y]:
            return dfs(nx,ny)


n,m = map(int,input().split())

arr = [[0]*m for _ in range(n)]
mapping = [[0]*m for _ in range(n)]

for _ in range(n):
    arr = list(map(int,input().split()))

for i in range(n):
    for j in range(m):
        dfs(i,j)

