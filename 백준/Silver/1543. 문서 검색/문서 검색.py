import sys
from collections import deque

# input = sys.stdin.readline

s = input()
w = input()
q = deque()

answer = 0
for i in s:
    if "".join(q) == w:
        answer += 1
        while q:
            q.popleft()

    if len(q) >= len(w):
        q.popleft()
    q.append(i)

if q and "".join(q) == w:
    answer += 1
print(answer)
