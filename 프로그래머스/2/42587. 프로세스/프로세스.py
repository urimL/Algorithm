from collections import deque

def solution(priorities, location):
    answer = 0
    MAX = max(priorities)
    q = deque()

    for p in range(len(priorities)):
        q.append([priorities[p], p])
    
    while q:
        now = q.popleft()
        if now[0] < MAX:
            q.append(now)
        else:
            answer += 1
            if now[1] == location:
                return answer
            MAX = max(q, key=lambda x: x[0])[0]
    
    return answer