def solution(s):
    t,answer = [],[]
    for i in s.split("},"):
        t.append(i.replace("{","").replace("}","").split(","))
        
    t.sort(key = lambda x:len(x))
    
    for i in t:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
                
    return answer
    