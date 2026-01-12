import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville) 
    
    # 섞을 음식이 2개 이상 있고, 가장 안 매운 놈이 k보다 작을 때만 반복
    while len(scoville) >= 2 and scoville[0] < k:
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        
        total = f + (s * 2)
        heapq.heappush(scoville, total)
        answer += 1
    
    # 루프가 끝났는데도 맨 앞(최솟값)이 k보다 작으면 실패
    return answer if scoville[0] >= k else -1