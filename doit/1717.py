import sys
input = sys.stdin.readline
n, m = map(int, input().split())
p = [ i for i in range(n+1)]

def union(f, t):
    f = find(f)
    t = find(t)
    if f != t:
        p[f] = t

def find(k):
    if k == p[k]:
        return k
    else:
        p[k] = find(p[k])
        return p[k]

for _ in range(m):
    c, f, t = map(int, input().split())

    if c == 0:
        union(f,t)
    else:
        a = find(f)
        b = find(t)
        if a == b:
            print('YES')
        else:
            print('NO')