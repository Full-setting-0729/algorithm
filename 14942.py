def create_table(node):
    chk[node] = 1

    for i in range(16):
        if parent[i][node]:
            anc,dist = parent[i][node]
            if parent[i][anc]:
                gnd_anc, gnd_dist = parent[i][anc]
                parent[i+1][node] = [gnd_anc,dist+gnd_dist]

    for b,c in arr[node]:
        if chk[b]:
            continue
        parent[0][b] = [node,c]
        create_table(b)

def arrive(node,energy):
    nn = node
    cost = 0
    for i in range(17):
        if parent[i][node]:
            anc_node,dist = parent[i][node]
            if dist <= energy:
                nn = anc_node
                cost = dist
            else:
                break
        else:
            break
    if nn == node:
        return
    return arrive(nn,energy-cost)
n = int(input())
parent = [[0]*100001 for _ in range(17)]
energy = [0]
chk = [0] * (n+1)
arr = [[]for _ in range(n+1)]
for i in range(n):
    energy.append(int(input()))

for _ in range(n-1):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

create_table(1)
for i in range(1,n+1):
    print(arrive(i,energy[i]))
