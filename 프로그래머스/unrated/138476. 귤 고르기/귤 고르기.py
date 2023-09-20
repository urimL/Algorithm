def solution(k, tangerine):
    answer = 0
    tmp = {}
    cnt = 0

    for i in tangerine:
        if i in tmp:
            tmp[i]+=1
        else:
            tmp[i]=1
        
    sorted_tmp=sorted(tmp,key=lambda x:tmp[x],reverse=True)
    
    for i in sorted_tmp:
        cnt+=tmp.get(i)
        answer+=1
        if cnt>=k:
            break

    return answer