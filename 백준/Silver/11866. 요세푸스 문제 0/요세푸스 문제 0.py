import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
pos = 1
answer = []

while q:
    if pos%k==0:
        answer.append(str(q.popleft()))
    else:
        q.append(q.popleft())
    pos+=1

print(f'<{", ".join(answer)}>')