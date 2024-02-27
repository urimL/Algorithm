import sys

input = sys.stdin.readline

x, y, w, s = map(int, input().split())
answer = 0

min_value = min(x, y)
max_value = max(x, y)

# 대각선이 더 빠른 경우
if w * 2 > s:
    if w > s:
        if abs(x - y) % 2 == 0:
            answer += min_value * s + abs(x - y) * s
        else:
            answer += min_value * s + (abs(x - y)-1) * s + w
    else:
        answer += min_value * s + abs(x - y) * w

# 대각선이 더 느린 경우
else:
    answer = (x + y) * w
print(answer)
