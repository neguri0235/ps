import sys
from collections import deque
n, r, c = map(int, input().split())
a = [['.' for _ in range(n)] for _ in range(n)]


q = deque()
q.append([r-1,c-1])

dx = [-1, -1, 1, 1]
dy = [-1, 1, 1, -1]

while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >=n:
            continue
        if a[nx][ny] == '.':
            a[nx][ny] = 'v'
            q.append([nx,ny])


for e in a:
    print(''.join(e))
    

