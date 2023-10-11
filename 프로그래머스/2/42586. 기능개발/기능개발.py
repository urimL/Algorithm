def solution(p,s):
    answer = []
    day,cnt = 0,0
    days = []
    q = []
    
    for i in range(len(p)):
        if (100-p[i])%s[i]!=0:
            day = (100-p[i])//s[i]+1
        else:
            day = (100-p[i])//s[i]
        
        days.append(day)
        
    for i in range(len(days)):
        if not q or q[0]>=days[i]:
            q.append(days[i])
            cnt+=1
        else:
            q.clear()
            answer.append(cnt)
            cnt = 1
            q.append(days[i])
    answer.append(cnt)
    
    return answer