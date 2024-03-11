import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, col):
    global ans

    for node in a[cur]:
        if mask[node] == -1:
            mask[node] = 1 - col
            dfs(node,1-col)
        else:
            if mask[node] == col:
                ans = False

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    a = [[] for _ in range(n+1)]
    for _ in range(m):
        f, t = map(int, input().split())
        a[f].append(t)
        a[t].append(f)

    mask = [-1 for _ in range(n+1)]
    ans = True
    for st in range(1,n+1):
        if mask[st] == -1:
            mask[st] = 0
            dfs(st,0)
    if ans:
        print('YES')
    else:
        print('NO')