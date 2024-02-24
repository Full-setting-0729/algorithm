n = int(input())

arr = [[]for _ in range(n+1)]

for _ in range(n):
    root,ch,cost = map(int,input().split())
    arr[root][ch] = cost
    arr[ch][root] = cost
    