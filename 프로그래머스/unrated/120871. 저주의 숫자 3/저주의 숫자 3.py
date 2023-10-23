def solution(n):
    answer = ''
    now = 1
    num = [0]*(n+1)
    for i in range(1,n+1):
        while '3' in str(now) or now%3==0:
            now+=1
        num[i]=now
        now+=1
    
    return num[-1]