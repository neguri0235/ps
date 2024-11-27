import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp =[[-1 for _ in range(2002)] for _ in range(2002)]
TC = int(input())


def go(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    if i == j:
        dp[i][j] = 1
        return dp[i][j]
    
    if i+1 == j:
        if A[i] == A[j]:
            dp[i][j] = 1
        else:
            dp[i][j] = 0
        
        return dp[i][j]

    if A[i] == A[j]:
        dp[i][j] = go(i+1, j-1)
    else:
        dp[i][j] = 0

    return dp[i][j]

for i in range(N):
    for j in range(i,N):
        go(i,j)

for _ in range(TC):
    fr, to = map(int, input().split())
    print(dp[fr-1][to-1])