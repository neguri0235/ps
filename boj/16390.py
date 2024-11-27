import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input().rstrip()))


def bfs(i, j):
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    q = deque()
    q.append([i,j])
    while q:
        x, y = q.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >=m:
                continue

            if a[nx][ny] == '#':
                a[nx][ny] = '.'
                q.append([nx,ny])



cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == '#':
            bfs(i,j)
            cnt += 1

print(cnt)