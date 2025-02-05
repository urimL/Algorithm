from collections import deque

def solution(q1, q2):
    answer = 0
    result = sum(q1) + sum(q2)
    q1 = deque(q1)
    q2 = deque(q2)
    
    if result%2 != 0 or max(q1) > result//2 or max(q2) > result//2:
        return -1
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    MAX = len(q1) + len(q2) * 2
    
    while sum_q1 != result//2 and answer < MAX:       
        if sum_q1 > sum_q2:
            now = q1.popleft()
            sum_q1 -= now
            sum_q2 += now
            q2.append(now)
            
        elif sum_q1 < sum_q2:
            now = q2.popleft()
            sum_q2 -= now
            sum_q1 += now
            q1.append(now)
        answer += 1 
    
    if sum_q1 != sum_q2:
        answer = -1
        
    return answer