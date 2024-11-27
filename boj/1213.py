import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

s = list(input().rstrip())

d = defaultdict(int)
for c in s:
    d[c] += 1

odd_count = 0
for i, v in d.items():
    if v % 2 == 1:
        odd_count += 1
dq = deque() 
if odd_count > 1:
    print('I\'m Sorry Hansoo')
else:
    for i , v in d.items():
        if v % 2 == 1:
            for k in range(v):
                dq.append(i)
    
    for i , v in d.items():
        if v % 2 == 0:
            for k in range(v//2):
                dq.append(i)
                dq.appendleft(i)
            
    print("".join(dq))

