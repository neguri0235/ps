import sys
input = sys.stdin.readline
dbg = 0

n, m = map(int, input().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
a = []
res = []

for _ in range(n):
    a.append([*input().rstrip()])


def check(x, y):
    k = 0
    while True:
        k += 1
        if x-k<0 or y-k<0 or x+k >=n or y+k>=m:
            k -= 1
            break
        if a[x-k][y] == '*' and a[x][y-k] == '*' and a[x+k][y] == '*' and a[x][y+k] == '*':
            dp[x][y] = 1
            dp[x-k][y] = 1
            dp[x][y-k] = 1
            dp[x+k][y] = 1
            dp[x][y+k] = 1
        else:
            k -=1
            break
    return k

for i in range(1, n):
    for j in range(1,m):
        if a[i][j] == '*':
            k = check(i,j)
            if k:
                res.append((i+1,j+1,k))

ans = 1
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            if dp[i][j] == 0:
                ans = -1
if ans != -1:
    print(len(res))
    for e in res:
        print(*e)
else:
    print(-1)

            
