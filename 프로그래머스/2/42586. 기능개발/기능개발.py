from collections import deque
def solution(progresses,speeds):
    answer = []
    q = deque()
    
    for p,s in zip(progresses, speeds):
        q.append([p,s])
        
    while q:
        cnt = 0
        for i in range(len(q)):
            p,s = q[i]
            if p < 100:
                q[i][0] += s
                
        while q and q[0][0] >= 100:
            cnt += 1
            q.popleft()
        
        if cnt > 0:
            answer.append(cnt)
                
    return answer