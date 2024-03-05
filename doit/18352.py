import sys
from collections import deque

n, m, k, x = map(int, input().split())
a = [[] for _ in range(n+1)]
for i in range(m):
    f, t = map(int, input().split())
    a[f].append(t)

q = deque([x])
v = [-1 for _ in range(n+1)]
v[x] = 0
while q:
    curr = q.popleft()
    for next in a[curr]:
        if v[next] >= 0: continue
        v[next] = v[curr]  + 1
        q.append(next)

res = []
for i in range(1,n+1):
    if v[i] == k:
        res.append(i)

if res:
    for e in res:
        print(e)
else:
    print(-1)
