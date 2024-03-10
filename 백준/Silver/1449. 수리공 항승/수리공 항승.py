import sys

input = sys.stdin.readline

n, l = map(int, input().split())
water = list(map(int, input().split()))
water.sort()

pos, answer = 0, 0
for w in water:
    if pos <= w:
        answer += 1
        pos = w - 0.5 + l

print(answer)
