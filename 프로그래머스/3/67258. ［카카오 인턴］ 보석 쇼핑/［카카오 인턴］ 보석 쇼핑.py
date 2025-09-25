def solution(gems):
    answer = []
    kind = len(set(gems))
    dic = {}
    start = 0
    
    for end in range(len(gems)):
        if gems[end] in dic:
            dic[gems[end]] += 1
        else:
            dic[gems[end]] = 1
        
        while len(dic) == kind:
            answer.append([start+1, end +1])
            dic[gems[start]] -= 1
            
            if dic[gems[start]] == 0:
                del dic[gems[start]]
            start += 1
            
    answer.sort(key = lambda x:x[1]-x[0])
    
    return answer[0]