def solution(n, s):
    if n > s:
        return [-1]
    nums = [s//n for _ in range(n)]
    total = 1
    remains = s - sum(nums)
    
    for i in range(n-1,-1,-1):
        if remains == 0:
            break
        nums[i] += 1
        remains -= 1
        
    return nums
    