import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

m, n = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input().rstrip()))
ans, temp = 0, 0


def go(x, y):
    global temp
    a[x][y] = '.'
    temp += 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >=n or ny >= m:
            continue

        if a[nx][ny] == '.':
            continue

        go(nx,ny)

for i in range(n):
    for j in range(m):
        temp = 0
        if a[i][j] == '*':
            go(i,j)

        ans = max(ans,temp)

print(ans)