import sys
import copy
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

TC = int(input())
dic = defaultdict(int)

def precalc():
    A = [ i+1 for i in range(8)]
    A = list(map(str, A))

    q = deque([A])


    while q:
        n = q.popleft()

        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                r = n[i:j+1]
                r.reverse()
                B = copy.deepcopy(n)
                for k in range(len(r)):
                    B[k+i] = r[k]

                fromkey = ''.join(n) 
                key = ''.join(B)
                if dic[key] == 0:
                    dic[key] = dic[fromkey] + 1
                    q.append(B)


precalc()

def solve(A):
    n = len(A)
    fixed = [i+1 for i in range(n)]

    for i in range(n):
        smaller = 0
        for j in range(n):
            if A[j] < A[i]:
                smaller += 1
        fixed[i] = smaller
    fixed = ''.join(list(map(str, fixed)))
    return dic[fixed]



for _ in range(TC):
    N = int(input())
    A = list(input().split())

    print(solve(A))
    
