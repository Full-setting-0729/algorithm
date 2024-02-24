import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n):
    arr.append(tuple(map(int,sys.stdin.readline().split())))

arr.sort()
result = 0
start = arr[0][0]
end = arr[0][1]

for i in range(n):
    if arr[i][0] <= end < arr[i][1]: #1 <= 3 < 3
        end = max(end,arr[i][1])
    elif arr[i][0] > end:
        result += end - start
        start = arr[i][0]
        end = arr[i][1]

result += end - start

print(result)


