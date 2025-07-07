def solution(nums):
    answer = 0
    dic = dict()
    total = len(nums)//2
    
    for n in nums:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    
    if len(dic) >= total:
        answer = total
    else:
        answer = len(dic)
    
    return answer