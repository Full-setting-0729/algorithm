import sys
import heapq
from collections import deque

INF = sys.maxsize
n,m = map(int,input().split())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dijk():
    distance = [INF for _ in range(n+1)]
    distance[1] = 0

    que = []
    heapq.heappush(que,[0,1])

    while que:
        cur_cost, cur_node = heapq.heappop(que)

        if distance[cur_node] < cur_cost:
            continue

        for nx_node, nx_cost in graph[cur_node]:
            if distance[nx_node] > nx_cost + cur_cost:
                distance[nx_node] = nx_cost + cur_cost
                heapq.heappush(que,[nx_cost+cur_cost,nx_node])

    return distance

distance = dijk()
edges = set()

def bfs():
    que = deque()
    que.append(n)

    while que:
        cur_node =que.popleft()

        if cur_node == 1: continue

        for post_node, post_cost in graph[cur_node]:
            if distance[post_node] + post_cost == distance[cur_node] and tuple((post_node, cur_node, post_cost)) not in edges:
                edges.add(tuple((post_node, cur_node, post_cost)))
                que.append(post_node)

bfs()


