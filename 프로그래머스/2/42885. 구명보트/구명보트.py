def solution(people, limit):
    answer = 0
    result = [False] * len(people)
    people.sort()
    
    start, end = 0, len(people)-1
    
    while start < end:
        s = people[start]+people[end]
        if  s <= limit:
            result[start], result[end] = True, True
            answer += 1
            start += 1
            
        end -= 1
    
    return answer + result.count(False)
