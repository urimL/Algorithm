def solution(people, limit):
    answer = 0
    n = len(people)
    
    people.sort()

    start, end = 0, n-1
    while start < end:
        if people[start] + people[end] <= limit:
            answer += 1
            start += 1
            end -= 1
        else:
            end -= 1
    
    answer += n - 2*answer
    
    
    return answer