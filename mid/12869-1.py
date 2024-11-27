import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
A = [0] * 3
dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]

for i in range(n):
    A[i] = a[i]


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

    dp[a][b][c] = 987654321

    dp[a][b][c] = min(go(a-9, b-3, c-1) + 1, dp[a][b][c])
    dp[a][b][c] = min(go(a-9, b-1, c-3) + 1, dp[a][b][c])

    dp[a][b][c] = min(go(a-1, b-9, c-3) + 1, dp[a][b][c])
    dp[a][b][c] = min(go(a-3, b-9, c-1) + 1, dp[a][b][c])

    dp[a][b][c] = min(go(a-1, b-3, c-9) + 1, dp[a][b][c])
    dp[a][b][c] = min(go(a-3, b-1, c-9) + 1, dp[a][b][c])

    return dp[a][b][c]

#print(*A)
print(go(A[0], A[1], A[2]))