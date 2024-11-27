import sys

input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]
A = [0]*3

for i in range(N):
    A[i] = p[i]

def go(a, b, c):
    if a < 0:
        return go(0, b, c)
    if b < 0:
        return go(a, 0, c)
    if c < 0:
        return go(a, b, 0)
    
    if dp[a][b][c] != -1:
        return dp[a][b][c]
    
    if a == 0 and b == 0 and c == 0:
        return 0
    
    ret = 987654321

    dp[a][b][c] = min(ret, go(a-9, b-3, c-1) + 1)
    ret = dp[a][b][c]
    dp[a][b][c] = min(ret, go(a-9, b-1, c-3) + 1)
    ret = dp[a][b][c]

    dp[a][b][c] = min(ret, go(a-1, b-9, c-3) + 1)
    ret = dp[a][b][c]
    dp[a][b][c] = min(ret, go(a-3, b-9, c-1) + 1)
    ret = dp[a][b][c]


    dp[a][b][c] = min(ret, go(a-1, b-3, c-9) + 1)
    ret = dp[a][b][c]
    dp[a][b][c] = min(ret, go(a-3, b-1, c-9) + 1)
    
    return dp[a][b][c]

print(go(A[0], A[1], A[2]))