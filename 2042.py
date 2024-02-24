import sys
sys.setrecursionlimit(1000001)


N,M,K = map(int,input().split())
num = [int(input()) for _ in range(N)]

seg_tree = [0 for _ in range(N*4)]

def buildtree(x,l,r):
    if l == r:
        seg_tree[x] = num[l]
        return seg_tree[x]
    mid = (l+r)//2
    l_value = buildtree(2*x,l,mid)
    r_value = buildtree(2*x+1,mid+1,r)
    seg_tree[x] = l_value+r+r_value
    return seg_tree[x]

buildtree(1,0,N-1)

def findtree(b,c,x,l,r):
    if c < l or r < b:
        return 0
    if b <= l and r <= c:
        return seg_tree[x]
    mid = (l+r)//2
    l_value = findtree(b,c,x*2,l,mid)
    r_value = findtree(b,c,x*2+1,mid+1,r)

    return l_value+r_value

def update_tree(x,l,r,i,val):
    if l == r == i:
        seg_tree[x] = val
        return
    if i < l or r < i:
        return
    mid = (l+r)//2

    update_tree(x*2,l,mid,i,val)
    update_tree(x*2+1,mid+1,i,val,r)

    seg_tree[x] = seg_tree[x*2] + seg_tree[x*2+1]

for _ in range(M+K):
    a,b,c = map(int,input().split())

    if a == 1:
        update_tree(1,0,N-1,b-1,c)
    else:
        s = findtree(b-1,c-1,1,0,N-1)
        print(s)
