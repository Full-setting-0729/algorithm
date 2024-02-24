from collections import deque

def bfs(a,b):



n,m = map(int,input().split())

graph = [[""]*m for _ in range(n+1)]

key = 0

for i in range(n+1):
    graph[i].append(list(map(input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j].islower():
            key += 1
