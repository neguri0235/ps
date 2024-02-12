import sys
import itertools
input = sys.stdin.readline

a, b =  input().split()
a, b = [*a], int(b)
a.sort()

ans = -1

for e in itertools.permutations(a):
    if e[0] == '0': continue
    temp = int(''.join(e))
    if temp < b:
        ans = max(temp, ans)

print(ans)
