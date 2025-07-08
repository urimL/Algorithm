def solution(clothes):
    answer = 1
    d = {}
    
    for c in clothes:
        name, category = c
        if category not in d:
            d[category] = [name]
        else:
            d[category].append(name)
    
    for i in d:
        answer *= len(d[i]) + 1 
        
    return answer -1