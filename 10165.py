n = int(input())
rectangles = []

for _ in range(n):
    x1, y1, x2, y2 = map(float, input().split())
    rectangles.append((x1, y1, x2, y2))

def calc_area(rectangles):
    total_area = 0
    for i, rect1 in enumerate(rectangles):
        total_area += (rect1[2] - rect1[0]) * (rect1[3] - rect1[1])
        for _, rect2 in enumerate(rectangles[i + 1:], start=i + 1):
            x1 = max(rect1[0], rect2[0])
            y1 = max(rect1[1], rect2[1])
            x2 = min(rect1[2], rect2[2])
            y2 = min(rect1[3], rect2[3])

            if x1 < x2 and y1 < y2:
                total_area -= (x2 - x1) * (y2 - y1)

    return total_area

total_area = calc_area(rectangles)

print(f"{total_area:.2f}")
