import sys
input = sys.stdin.readline
h, w = map(int, input().split())
n = int(input())
a = []
for _ in range(n):
    a.append([*map(int, input().split())])

ans = 0

dbg = 0

for i in range(n-1):
    for j in range(i+1,n):
        temp = 0

        # case 1
        r1, c1 = a[i]
        r2, c2 = a[j]

        if dbg:
            print('-----')
            print(r1,c1, r2,c2)
            print('-----')

        if (r1 + r2) <= h and max(c1,c2) <= w:
            temp = r1*c1 + r2*c2
            ans = max(temp, ans)
        r1, c1 = c1, r1
        if (r1 + r2) <= h and max(c1,c2) <= w:
            temp = r1*c1 + r2*c2
            ans = max(temp, ans)
        r2, c2 = c2, r2
        if (r1 + r2) <= h and max(c1,c2) <= w:
            temp = r1*c1 + r2*c2
            ans = max(temp, ans)
        r1, c1 = c1, r1
        if (r1 + r2) <= h and max(c1,c2) <= w:
            temp = r1*c1 + r2*c2
            ans = max(temp, ans)

        # case 2
        r1, c1 = a[i]
        r2, c2 = a[j]

        if (c1+ c2) <= w and max(r1,r2) <= h:
            temp = r1*c1 + r2*c2
            ans = max(temp, ans)
        r1, c1 = c1, r1
        if (c1+ c2) <= w and max(r1,r2) <= h:
            temp = r1*c1 + r2*c2
            ans = max(temp, ans)
        r2, c2 = c2, r2
        if (c1+ c2) <= w and max(r1,r2) <= h:
            temp = r1*c1 + r2*c2
            ans = max(temp, ans)
        r1, c1 = c1, r1
        if (c1+ c2) <= w and max(r1,r2) <= h:
            temp = r1*c1 + r2*c2
            ans = max(temp, ans)

        # case 3

        # case 4
    

print(ans)

