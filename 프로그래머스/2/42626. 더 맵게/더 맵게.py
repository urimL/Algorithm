import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        first = heapq.heappop(scoville)
        if first >= k:
            return answer
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1