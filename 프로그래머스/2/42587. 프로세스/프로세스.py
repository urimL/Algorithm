from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    
    for idx, p in enumerate(priorities):
        q.append([idx, p])
    
    while q:
        idx, p = q.popleft()
        if any(p < other[1] for other in q):
            q.append([idx, p])
        else:
            answer += 1
            if location == idx:
                return answer
    