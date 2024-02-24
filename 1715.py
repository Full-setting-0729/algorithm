def up(k):
    if k // 2 == 0:
        return
    if x[k//2] > x[k]:
        temp = x[k//2]
        x[k//2] = x[k]
        x[k] = x[k//2]
        up(k//2)

def down(k):
    sw = k * 2
    if sw + 1 < len(x) and x[sw] > x[sw + 1]: # 오른쪽 자식이 있고 더 작다면 변경
        sw += 1
    if x[k] > x[sw]:
        temp = x[k]
        x[k] = x[sw]
        x[sw] = temp
        down(sw)


n = int(input())
x = [0] #heap
for _ in range(n):
    x = int(input())
    up(len(x))
    result = + x.pop(1)





