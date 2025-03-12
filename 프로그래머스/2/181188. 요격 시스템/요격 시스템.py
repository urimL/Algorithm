def solution(targets):
    answer = 0
    targets.sort()
    now = [-1,-1]
    
    for t in targets:
        if now[1] > t[0]:
            now = [max(now[0], t[0]),min(now[1], t[1])]

        elif now[1] <= t[0]:
            answer += 1
            now = t
        
        
        
    return answer