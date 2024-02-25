import sys
import math

input = sys.stdin.readline

n, t = map(int, input().split())
bus = []
for i in range(n):
    bus.append(list(map(int, input().split())))
answer, min_time = 0, 1000001

for b in bus:
    s, l, c = b

    if t <= s:
        min_time = min(min_time, s - t)

    else:
        wait = math.ceil((t - s) / l)

        if wait > c or s + l * (c - 1) < t:
            continue

        wait = s + (wait * l) - t
        min_time = min(min_time, wait)

if min_time == 1000001:
    min_time = -1
print(min_time)
