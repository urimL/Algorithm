def solution(food):
    answer = ''
    pos=1
    
    for i in range(1,len(food)):
        answer+=str(pos)*(food[i]//2)
        pos+=1
        
    tmp=answer[::-1]
    answer+='0'
    answer+=tmp
        
    
    return answer