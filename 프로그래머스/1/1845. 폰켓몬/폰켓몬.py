def solution(nums):
    answer = 0
    d = len(set(nums))
    
    if d>=len(nums)//2:
        answer=len(nums)/2
    else:
        answer=d
        
    
    return answer