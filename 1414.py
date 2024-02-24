INF = 200000
MA = 51

map = [[INF for _ in range(MA)] for _ in range(MA)]
chk = [0] * MA
dis = [0] * MA
N = 0
M = 0
n = 0
m = 0
dab = 0
sum = 0

def prim():
    global dab, sum
    global N

    global map
    global chk
    global dis

    min_val = INF
    k = -1
    mink = 0

    chk[1] = 1

    for i in range(1, N + 1):
        dis[i] = map[1][i]
        if chk[i] == 0 and min_val > dis[i]:
            min_val = dis[i]
            k = i

    for i in range(1, N):
        if k == -1:
            dab = -1
            return

        dab += min_val
        chk[k] = 1
        mink = -1
        min_val = INF

        for j in range(1, N + 1):
            if chk[j] == 0 and dis[j] > map[k][j]:
                dis[j] = map[k][j]

            if chk[j] == 0 and min_val > dis[j]:
                min_val = dis[j]
                mink = j

        k = mink

    dab = sum - dab

def main():
    global N
    global sum

    global map

    N = int(input())

    for i in range(1, N + 1):
        row_input = input()
        for j in range(1, N + 1):
            t = row_input[j - 1]
            if t >= 'A' and t <= 'Z':
                temp = ord(t) - 38
            elif t >= 'a' and t <= 'z':
                temp = ord(t) - 96
            else:
                temp = INF

            if i != j and map[i][j] > temp:
                map[i][j] = map[j][i] = temp

            if temp != INF:
                sum += temp

    prim()
    print(dab)

if __name__ == "__main__":
    main()