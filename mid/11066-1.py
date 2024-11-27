import sys
input = sys.stdin.readline

tc = int(input())


def go(n, a, dp, i, j):

    if i == j:
        dp[i][j] = 0
        return dp[i][j]
    
    if dp[i][j] != -1:
        return dp[i][j]

    sum = 0 
    for k in range(i, j+1):
        sum += a[k]

    for k in range(i, j+1):
        temp = go(n, a, dp, i, k) + go(n, a, dp, k+1, j) + sum

        if temp < dp[i][j] or dp[i][j] == -1:
            dp[i][j] = temp
    
    return dp[i][j]



for _ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[-1 for _ in range(502)] for _ in range(502)]
    print(go(n,a,dp,0,n-1))