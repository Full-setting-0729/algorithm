import math

infi = math.inf

N = int(input())
M = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]
dis = []
v = []
chk = []

for _ in range(M):
    a,b,c = list(map(int,input().split()))
    graph[a-1][b-1] = c


start,end = map(int,input().split())



def dfs(v):
    if v == 0:
        return
    dfs(v[v])
    
