import sys
from collections import deque

n, k, m = map(int, input().split())

a = [[] for _ in range(m)]
b = [[] for _ in range(n+1)]

for i in range(m):
    a_ = list(map(int, input().split()))

    for e in a_:
        a[i].append(e)
        b[e].append(i)

dbg = False

if dbg:
    for e in a:
        print(e)
    print('-----')
    for e in b:
        print(e)

v = [-1 for _ in range(n+1)]
v[1] = 1

q = deque()
q.append(1)


while q:
    cur = q.popleft()
    step = v[cur]

    for loop in b[cur]:
        for node in a[loop]:
            if v[node] == -1:
                v[node] = step + 1
                q.append(node)
#print(v)
print(v[n])