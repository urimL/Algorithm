import heapq

def solution(jobs):
    answer,i = 0,0
    hq = []
    start, now = -1,0

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(hq, [j[1],j[0]])
                
        if hq:
            x,y = heapq.heappop(hq)
            start = now
            now += x
            answer += now-y
            i +=1
        else:
            now += 1
    
    return answer // len(jobs)