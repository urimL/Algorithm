def solution(p):
    answer = ''
    x = list(p.split(" + "))
    x_cnt,n_cnt = 0,0
    
    for i in x:
        if i[-1]=='x':
            if len(i)==1:
                x_cnt+=1
            else:
                num = "".join(i[0:-1])
                x_cnt+=int(num)
        else:
            n_cnt+=int(i)     
    
    if x_cnt==0:
        answer=answer+(str(n_cnt)) if n_cnt>0 else answer+'0'
    elif x_cnt==1:
        answer=answer+('x + '+str(n_cnt)) if n_cnt>0 else answer+'x'
    else:
        answer=answer+(str(x_cnt)+'x + '+str(n_cnt)) if n_cnt>0 else answer+(str(x_cnt)+'x')
    return answer