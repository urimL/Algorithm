from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    min_p = min(priorities)
    
    for i, p in enumerate(priorities):
        q.append([i,p])
        
    print(q)
    
    while q:
        idx, p = q.popleft()
        if any(p < other[1] for other in q):
            q.append([idx,p])
            
        else:
            answer += 1
        
            if idx == location:
                break

    return answer