def solution(numbers):
    answer = 0
    nums = set()
    list = set([0,1,2,3,4,5,6,7,8,9])
    for n in numbers:
        if n not in nums:
            nums.add(n)
    
    answer = sum(list - nums)
    return answer