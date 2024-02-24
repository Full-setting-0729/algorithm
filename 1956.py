INF = int(1e19)

v,e = map(int,input().split())

graph = [[INF]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(v+1):
    for i in range(v+1):
        for j in range(v+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer = INF
for i in range(1, v+1):
    #사이클은 결국 출발지와 도착지가 같은 경우이므로 i->i를 확인
    answer = min(answer, graph[i][i])

#최소값이 없으면 -1, 있으면 최소값을 출력
if answer == INF:
    print(-1)
else:
    print(answer)