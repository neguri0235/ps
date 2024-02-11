import sys
input = sys.stdin.readline

n, l, r, x = map(int, input().split())
a = [*map(int, input().split())]
check = [0] * 17
ans = 0

def go(idx, cnt, sum, easy, hard):
    if idx == n:
        if cnt >= 2 and  sum >= l and sum <= r and (hard - easy) >= x:
            return 1
        else:
            return 0

    temp1 = go(idx+1, cnt+1, sum + a[idx], min(easy, a[idx]), max(hard, a[idx]))
    temp2 = go(idx+1, cnt, sum, easy,hard)

    return temp1 + temp2

ans = go(0,0,0,sys.maxsize,0)
print(ans)