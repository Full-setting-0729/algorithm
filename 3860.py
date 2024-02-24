INF = float('inf')

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    g = int(input())

    graph = [[0 for _ in range(h)] for _ in range(w)]

    hole = [[INF,INF,INF]]
    for _ in range(g):
        x,y = map(int,input().split())
        graph[x][y] = -1
    #귀신구멍 갯수
    e = int(input())
    #귀신구멍의 정보
    #x1,y1=귀신구멍 좌표,x2,y2 = 나오는 좌표, t = 코스트
    for i in range(1,e+1):
        x1,y1,x2,y2,t = map(int,input().split())
        graph[x1][y1] = i
        hole.append([x2,y2,t])
dist = [[INF for _ in range(h)] for _ in range(w)]

dist[0][0] = 0

def bellmanford():
    for cnt in range(h*w):
        for x in range(w):
            for y in range(h):
                #묘비거나 도착점이거나 귀신구멍 처리
                if x == w-1 and y == h-1 or graph[x][y] == -1:
                    continue
                elif graph[x][y] >= 1:
                    oX,oY,oT = hole[graph[x][y]]
                    if dist[oX][oY] > dist[x][y] + oT:
                        dist[oX][oY] = dist[x][y] + oT

                        if cnt == h*w-1:
                            return float('-inf')

                elif graph[x][y]==0:
                    for nx,ny in ([x,y+1], [x,y-1], [x+1,y], [x-1,y]):
                        if 0 <= nx < w and 0 <= ny < h :
                            if graph[nx][ny] >= 0 :
                                if dist[nx][ny] > dist[x][y]+1:
                                    dist[nx][ny] = dist[x][y]+1

                                    if cnt == h*w-1:
                                        return float('-inf')


            return dist[w-1][h-1]

        result = bellmanford()

        if result == INF:
            print("Impossible")
        elif result == float('-inf'):
            print("Never")
        else:
            print(result)


