import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(m):
    a.append(list(map(int, input().split())))

dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]


def go(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    if x == y:
        return 0
    
    if x+1 == y:
        dp[x][y] = a[x][0] * a[x][1] * a[y][1]
        return dp[x][y]
    
    for k in range(x, y):
        t1 = go(x,k)
        t2 = go(k+1,y)

        if dp[x][y] == -1 or dp[x][y] > t1 + t2 + (a[x][0] * a[k][1] * a[y][1]):
            dp[x][y] = t1 + t2 + (a[x][0] * a[k][1]*a[y][1])
        
    return dp[x][y]


print(go(0, n-1))

