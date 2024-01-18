def solution(n, times):
    start, end = 1, max(times) * n
    answer = 0
    
    while start <= end:
        mid = (start+end)//2
        result = 0
        
        for t in times:
            result += mid//t
            if result > n:
                break
        
        if result < n:
            start = mid+1
        else:
            answer = mid
            end = mid-1
    
    return answer
    