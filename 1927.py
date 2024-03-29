import sys
def up(k):
    if k // 2 == 0:
        return
    if heap[k//2] > heap[k]:
        temp = heap[k//2]
        heap[k//2] = heap[k]
        heap[k] = temp
        up(k//2)
def down(k):
    sw = k * 2
    if sw + 1 < len(heap) and heap[sw] > heap[sw + 1]: # 오른쪽 자식이 있고 더 작다면 변경
        sw += 1
    if heap[k] > heap[sw]:
        temp = heap[k]
        heap[k] = heap[sw]
        heap[sw] = temp
        down(sw)

n = int(input())
heap = [0]

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 1:
            print(0)
        else:
            temp = heap[1]
            heap[1] = heap[-1]
            heap[-1] = temp
            print(heap.pop(-1))
            down(1)
    else:
        heap.append(num)
        up(len(heap)-1)