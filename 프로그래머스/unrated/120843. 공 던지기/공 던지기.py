def solution(numbers, k):
    answer = 0
    pos = 0
    
    for i in range(k-1):
        pos+=2
        if pos>=len(numbers):
            pos%=len(numbers)
        print(pos)
    answer = numbers[pos]
    return answer