import sys
import collections
input = sys.stdin.readline

sender = [0, 0, 1, 1, 2, 2]
receiver =   [1, 2, 0, 2, 0, 1]

a = [*map(int, input().split())]
vis = [ [False for _ in range(201)] for _ in range(201)]
ans = [False] * 201

def BFS():
    q = collections.deque()
    q.append((0,0))
    vis[0][0] = True
    ans[a[2]] = True

    while q:
        now = q.popleft()
        A, B = now[0], now[1]
        C = a[2] - A - B
        for k in range(6):
            next = [A, B, C]
            next[receiver[k]] += next[sender[k]]
            next[sender[k]] = 0

            if next[receiver[k]] > a[receiver[k]]:
                next[sender[k]] = next[receiver[k]] - a[receiver[k]]
                next[receiver[k]] = a[receiver[k]]
            
            if not vis[next[0]][next[1]]:
                vis[next[0]][next[1]] = True
                q.append((next[0], next[1]))
                if next[0] == 0:
                    ans[next[2]] = True
BFS()

for i in range(len(ans)):
    if ans[i]:
        print(i,end = ' ')

