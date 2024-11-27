import sys
input = sys.stdin.readline

dp = [-1 for _ in range(102)]

N = int(input())

dp[0], dp[1], dp[2], dp[3], dp[4]= 0, 1, 2, 3, 4

for i in range(1, N+1):
    dp[i] = dp[i-1] + 1
    for j in range(1, i-3+1):
        dp[i] = max(dp[i], dp[i-j-2]*(j+1))

print(dp[N])