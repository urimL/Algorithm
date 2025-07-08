import math
def solution(progresses, speeds):
    answer = []
    days = []
    
    for p,s in zip(progresses, speeds):
        days.append([p,math.ceil((100-p)/s)])
    
    days = days[::-1]
    print(days)
    now = days.pop()[1]
    cnt = 1
    while days:
        tmp = days.pop()[1]
        if now >= tmp:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            now = tmp
    answer.append(cnt)
    return answer