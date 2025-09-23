def solution(s):
    answer = []
    result = []
    
    s = s.split("},")
    for i in s:
        tmp = i.replace("{","").replace("}","").split(",")
        result.append(tmp)
        
    result.sort(key = len)

    for r in result:
        for i in r:
            if i not in answer:
                answer.append(i)
    
    answer = list(map(int,answer))
    return answer
    
