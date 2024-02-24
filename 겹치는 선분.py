import sys

n = int(input())
points = []


for _ in range(n):
    points.append(tuple(map(int,sys.stdin.readline().split())))

points.sort()