def solution(array, n):
    answer = 0
    result = 1000
    
    array.sort(reverse=True)
    
    for i in array:
        if abs(n-i)<=result:
            result = abs(n-i)
            answer=i
    return answer