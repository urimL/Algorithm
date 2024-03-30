def solution(stones, k):
    answer = 0
    n = len(stones)
    
    start, end = min(stones), max(stones)
    
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for s in stones:
            if s-mid <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                break
            
        if cnt < k:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    
    return answer