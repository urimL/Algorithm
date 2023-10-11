import heapq

def solution(n, works):
    if sum(works) <= n :
        return 0
    
    answer = 0
    
    works = [-w for w in works]
    heapq.heapify(works) #work를 힙으로 변환
    
    for i in range(n):
        max_v = heapq.heappop(works)
        heapq.heappush(works, max_v+1)
    
    for i in works:
        answer+=i**2
        
    return answer