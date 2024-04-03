def solution(scores):
    answer = 0
    target = scores[0]
    max_score = sum(scores[0])
    
    scores.sort(key = lambda x:(-x[0],x[1]))
    max_b = 0
    
    for s in scores:
        if target[0] < s[0] and target[1] < s[1]:
            return -1
        
        if max_b <= s[1]:
            max_b = s[1]
            if max_score < sum(s):
                answer += 1
        
    
    return answer+1