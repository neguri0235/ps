import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())

a = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

v = [0 for _ in range(n+1)]

for i in range(1,n+1):
    a[i].sort()

q = deque()
q.append(r)

cnt = 1

v[r] = cnt

while q:
    cur = q.popleft()

    for e in a[cur]:
        if v[e]:
            continue
        cnt += 1
        v[e] = cnt 
        q.append(e)

for i in range(1,n+1):
    print(v[i])




