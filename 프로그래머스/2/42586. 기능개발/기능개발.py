from collections import deque
def solution(progresses,speeds):
    answer = []
    q = deque()
    cnt = 0
    
    for i in range(len(speeds)):
        if (100-progresses[i])%speeds[i] == 0:
            day = (100-progresses[i])//speeds[i]
        else:
            day = (100-progresses[i])//speeds[i]+1
        q.append(day)

    while q:
        now = q.popleft()
        answer.append(1)
        
        while q:
            if q and now >= q[0]:
                answer[-1] += 1
                q.popleft()
            else:
                break
    
    print(answer)
    return answer
            