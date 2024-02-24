import sys

INF = sys.maxsize

n, m = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append([v,w])

def bellman_ford(start):
    dist = [-INF for _ in range(n+1)]
    dist[start] = 0
    path = [0 for _ in range(n+1)]

    for i in range(n):
        for cur_node in range(1,n+1):
            for nx_node,nx_cost in graph[cur_node]:
                if dist[cur_node] != -INF and dist[nx_node] < nx_cost+dist[cur_node]:
                    #사이클 아님 업데이트
                    dist[nx_node] = nx_cost + dist[cur_node]
                    path[nx_node] = cur_node

                    #사이클 존재하면 무한대 표시
                    if i == n-1:
                        dist[nx_node] = INF

    result = []
    cur_node = n

    #사이클 존재
    if dist[n] == INF:
        print(-1)
        return
    while cur_node != 1:
        result.append(cur_node)
        cur_node = path[cur_node]
    result.append(cur_node)
    result = result[::-1]
    print(*result,end= " ")
    return
bellman_ford(1)





