def solution(gems):
    answer = []
    category = len(set(gems))
    gemNow = dict()
    start = 0
    
    for i in range(len(gems)):
        if gems[i] not in gemNow:
            gemNow[gems[i]] = 1
        else:
            gemNow[gems[i]] += 1
        
        while len(gemNow) == category:
            answer.append([start+1, i+1])
            gemNow[gems[start]] -= 1
            
            if gemNow[gems[start]] == 0:
                del gemNow[gems[start]]
            start += 1  
    
    answer.sort(key = lambda x:(x[1] - x[0], x[0]))
    
    return answer[0]