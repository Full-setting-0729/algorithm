n = int(input())

line = [[0] for _ in range(n)]

for i in range(n):
    x1,y1,x2,y2  = map(int,input().split())
    line[i] = (x1,y1,x2,y2)