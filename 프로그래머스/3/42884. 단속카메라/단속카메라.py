def solution(routes):
    answer = 0
    
    start, end = -30001,30001
    routes.sort()
    tmp = [0,0]
    
    for i in range(len(routes)):
        if i == len(routes)-2:
            tmp = routes[i]
            
        if end >= routes[i][0]:
            start, end = max(start, routes[i][0]), min(end, routes[i][1])
        else:
            answer += 1
            start, end = routes[i]
            
    if [start, end] != tmp:
        answer += 1
        
    return answer