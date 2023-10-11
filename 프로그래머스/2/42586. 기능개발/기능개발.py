def solution(p,s):
    answer = []
    day,cnt = 0,0
    days = []
    st = []
    
    for i in range(len(p)):
        if (100-p[i])%s[i]!=0:
            day = (100-p[i])//s[i]+1
        else:
            day = (100-p[i])//s[i]
        
        days.append(day)
        
    for i in range(len(days)):
        if not st or st[0]>=days[i]:
            st.append(days[i])
            cnt+=1
        else:
            while st:
                st.pop()
            answer.append(cnt)
            cnt = 1
            st.append(days[i])
    answer.append(cnt)
    
    return answer