import sys
input = sys.stdin.readline

a, b, c, x, y = map(int, input().split())

ans1, ans2, ans3 = 0, 0, 0

ans1 = a*x + b*y

while x and y:
    x-=1
    y-=1
    ans2 += c*2
ans3 = ans2 +(x*c*2) + (y*c*2)
ans2 += a*x + b*y

print(min(ans1, ans2, ans3))