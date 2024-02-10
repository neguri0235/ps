import sys
dp = [0] * 1002

a = [1, 5, 10, 50]

def go(idx, cnt, sum):

    if cnt == n:
        dp[sum] = 1
        return

    for k in range(idx, 4):
        go(k, cnt + 1, sum + a[k])


n = int(input())

go(0,0,0)
dp[0] = 0
print(dp.count(1))