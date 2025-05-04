from itertools import combinations

def solution(clothes):
    answer = 0
    dic = dict()
    
    for c in clothes:
        name, category = c
        if category in dic.keys():
            dic[category].append(name)
        else:
            dic[category] = [name]
    
    cnt = 1
    for key in dic.keys():
        cnt *= (len(dic[key])+1)
    
    answer += cnt   
    
    return answer-1
            