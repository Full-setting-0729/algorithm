def dfs()

v = int(input())

arr = [[]for _ in range(v+1)]

for i in range(v):
    line = list(map(int,input().split()))
    start_node = line[0]
    index = 1
    while line[index] != -1:
        pal_node,pal_cost = line[index],line[index+1]
        arr[start_node].append((pal_node,pal_cost))
        index+=2
visited = [-1]*(v+1)
visited[1] = 0




