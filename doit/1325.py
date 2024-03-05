import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
for _ in range(m):
    f, t = map(int, input().split())
    A[t].append(f)
ans = 0

cnt = [0] * (n+1)

for i in range(1,n+1):
    v = [0] * (n+1)

    v[i] = 1
    q = deque([i])
    while q:
        cur = q.popleft()
        for node in A[cur]:
            if v[node]: continue
            v[node] = 1
            q.append(node)
            cnt[i] += 1
max = max(cnt)
for i in range(1,n+1):
    if cnt[i] == max:
        print(i,end = ' ')