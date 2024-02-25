import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
rotate = []
answer = 0

for w in words:
    if not rotate:
        rotate.append(w)
    else:
        check = False
        for r in rotate:
            for i in range(len(r)):
                q = deque(r)
                q.rotate(i)
                if "".join(q) == "".join(w):
                    check = True
                    break
        if not check:
            rotate.append(w)

print(len(rotate))
