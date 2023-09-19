def solution(s):
    s=list(s)
    answer = -1
    tmp = []
    
    for i in range(len(s)):
        if len(tmp)==0:
            tmp.append(s[i])
        elif tmp[-1]==s[i]:
            tmp.pop()
        else:
            tmp.append(s[i])
            
    if len(tmp)==0:
        answer=1

    else:
        answer=0

    return answer