def solution(numbers, target):

    
    def check(now, idx):

        if idx == len(numbers):
            return 1 if now == target else 0

        op1 = check(now + numbers[idx], idx+1)
        op2 = check(now - numbers[idx], idx+1)
        
        return op1 + op2
    
    return check(0,0)