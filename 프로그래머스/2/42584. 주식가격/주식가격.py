from collections import deque
def solution(prices):
    time = []
    q = deque(prices)
    
    while q:
        price = q.popleft()
        t = 0
        for i in q:
            t += 1
            if price > i:
                break
        time.append(t)        
        
    return time