def solution(seoul):
    answer = 0
    
    for i in seoul:
        if i=="Kim":
            answer=seoul.index(i)
            
    return "김서방은 "+str(answer)+"에 있다"