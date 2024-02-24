
zero_cnt = []
one_cnt = []
zero = 0
one = 0
def fibo(v):
    if memo[v] != -1:
        return memo[v]
    if v == 0:
        zero_cnt[v] += 1
        memo[v] = 0
        return 0
    if v == 1:
        one_cnt[v] += 1
        memo[v] = 0
        return 1
    memo[v] = fibo(v-2) + fibo(v-1)
    return memo[v]

n = int(input())
memo = [-1] * (n + 1)
print(zero_cnt,one_cnt)







