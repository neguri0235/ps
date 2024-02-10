import sys
input = sys.stdin.readline
n = int(input())
a = [*map(int, input().split())]

dp = []

for e in a:
    cnt = 0
    k = e
    while e:
        if not e%3:
            e = e//3
            cnt += 1
        else:
            break
    dp.append([cnt,k])
dp.sort(key = lambda x :(-x[0],x[1]))
#print(dp)
for e in dp:
    print(e[1],end = ' ')