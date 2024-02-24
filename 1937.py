def dfs(x,y):
    if dp[x][y] == 0:
        dp[x][y] = 1
    else:
        return
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:
            dfs(nx,ny)
        else:
            dp[x][y] += 1
            return dp[x][y]

n = int(input())

arr = [[0]*n for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        dfs(i,j)

print(max(dp))