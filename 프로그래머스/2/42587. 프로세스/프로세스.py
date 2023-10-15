from collections import deque

def solution(p, location):
    answer = 0
    q = deque()
    
    for i in range(len(p)):
        q.append(i)
        
    while q:
        process = q.popleft()
        priority = p.pop(0)
        
        if p:
            if priority >= max(p):
                answer+=1
                if process == location:
                    break

            else:
                q.append(process)
                p.append(priority)
        
        else:
            answer+=1
        
                    
    return answer