import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    while n > 0:
        now = heapq.heappop(works)
        heapq.heappush(works, now + 1)
        n -= 1
    
    answer = sum(x**2 for x in works)
        
    return answer