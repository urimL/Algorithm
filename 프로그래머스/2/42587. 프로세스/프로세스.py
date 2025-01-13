from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque()
    
    #[프로세스, 우선순위]
    for i in range(len(priorities)):
        q.append([i, priorities[i]])
        
    while q:
        max_p = max(q, key = lambda x:x[1])[1]
        num, p = q.popleft()
        if p >= max_p:
            if num == location:
                break
            else:
                answer += 1
        else:
            q.append([num,p])

    return answer