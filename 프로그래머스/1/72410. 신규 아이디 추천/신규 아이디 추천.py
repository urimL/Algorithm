def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    for s in new_id:
        if 'a'<=s<="z" or '0'<=s<='9' or s=='-' or s=="_" or s==".":
            answer += s
        
    while ".." in answer:
        answer = answer.replace("..", ".")
        
    answer = answer.strip('.')
    
    if not answer:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip(".")
    
    
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer