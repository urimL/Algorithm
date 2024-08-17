import heapq
def solution(scoville, k):
    answer = 0
    hq = []
    
    for s in scoville:
        heapq.heappush(hq,s)
        
    while True:
        if hq[0] < k:
            now = heapq.heappop(hq)

            if hq:
                new = now + heapq.heappop(hq)*2
            else:
                return -1
            
            heapq.heappush(hq, new)
            answer += 1
            
        else:
            return answer
