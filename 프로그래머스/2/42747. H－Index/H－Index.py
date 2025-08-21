def solution(citations):
    answer = 0
    total = len(citations)
    
    citations.sort()

    for i in range(len(citations)):
        if citations[i] > total - i:
            answer = max(answer, total - i)
            break
        if citations[i] >= i: 
            answer = citations[i]
        
    if answer == 0:
        answer = min(total, citations[0])
    return answer