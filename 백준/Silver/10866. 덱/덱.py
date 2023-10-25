import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    command = list(map(str,input().split()))

    if command[0]=='push_front':
        q.appendleft(command[1])

    elif command[0]=='push_back':
        q.append(command[1])
                 
    elif command[0]=='pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
            
    elif command[0]=='pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)

    elif command[0]=='size':
        print(len(q))
        
    elif command[0]=='empty':
        if q:
            print(0)
        else:
            print(1)
            
    elif command[0]=='front':
        if q:
            print(q[0])
        else:
            print(-1)
            
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
