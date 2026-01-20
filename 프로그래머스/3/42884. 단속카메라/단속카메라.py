def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x:x[1])
    start, end = -30001, -30001
    
    for s,e in routes:
        if end < s:
            answer += 1
            start, end = s, e

    return answer