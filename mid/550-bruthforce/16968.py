import sys
input = sys.stdin.readline

a = [*input().rstrip()]

ans = 1
p = ' ' 

for i in range(len(a)):
    
    if a[i] == 'c':
        if p == 'c':
            ans *= 25
        else:
            ans *= 26
    else:
        if p == 'd':
            ans *= 9
        else:
            ans *= 10
    p = a[i]
print(ans)