def timeCheck(d, t, limit, level):
    result = 0
    for i in range(len(d)):
        if d[i] <= level:
            result += t[i]
        else:
            if i > 0:
                result += t[i] + (t[i-1] + t[i]) * (d[i] - level) 
    return result
                
    
def solution(diffs, times, limit):
    answer = 0
    if sum(times) == limit:
            return max(diffs)
    
    start, end = 1, max(diffs)
    
    while start <= end:
        mid = (start + end) // 2
        result = timeCheck(diffs, times, limit, mid)
        if result > limit:
            start = mid + 1
        elif result <= limit:
            end =  mid - 1
            answer = mid 

    return answer