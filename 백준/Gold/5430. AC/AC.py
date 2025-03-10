import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    q = deque(list(input().rstrip()[1:-1].split(",")))
    check = True
    answer = ''

    if n == 0:
        q = deque()

    cnt = 0        
    for c in p:
        if c == "R":
            cnt += 1
                
        else:
            if not q:
                check = False
                break
            else:
                if cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if not check:
        answer = "error"
    else:
        if cnt % 2 == 0:
            answer = ("["+",".join(q)+"]")
        else:
            q.reverse()
            answer = ("["+",".join(q)+"]")

    print(answer)
        
                
            
