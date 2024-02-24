import heapq
import sys

def dijk(start):
    que = []
    heapq.heappush(que,(0,start))
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            ref = dist + i[1]
            if ref < distance[i[0]]:
                distance[i[0]] = ref
                heapq.heappush(que,(ref,i[0]))
input = sys.stdin.readline
INF = sys.maxsize

v,e = map(int,input().split())
start = int(input())

distance = [INF] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

dijk(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
