import sys
from collections import deque
b1, b2 = map(int, input().split())
d1, d2 = map(int, input().split())
c1, c2 = map(int, input().split())



dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

b_cnt = 0
cnt = 0
q = deque()
q.append([b1,b2,cnt])

a = [[0 for _ in range(1001)] for _ in range(1001)]

a[b1][b2] = 1

while q:
    x, y, z = q.popleft()
    if x == c1 and y == c2:
        b_cnt = z
        break
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx > 1000 or ny > 1000:
            continue
        if a[nx][ny] == 0:
            a[nx][ny] = 1
            q.append([nx,ny,z+1])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
d_cnt = 0
q = deque()
q.append([d1,d2,cnt])

a = [[0 for _ in range(1001)] for _ in range(1001)]

a[d1][d2] = 1

while q:
    x, y, z = q.popleft()
    if x == c1 and y == c2:
        d_cnt = z
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx > 1000 or ny > 1000:
            continue
        if a[nx][ny] == 0:
            a[nx][ny] = 1
            q.append([nx,ny,z+1])


if b_cnt < d_cnt:
    print('bessie')
elif b_cnt > d_cnt:
    print('daisy')
else:
    print('tie')