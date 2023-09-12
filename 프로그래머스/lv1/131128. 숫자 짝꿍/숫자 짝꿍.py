def solution(X, Y):
    answer = ''
    tmp=0
    
    #가장 큰 정수를 만들어야 하므로 뒤에서 부터 시작
    for i in range(9,-1,-1):
        # 값 (0~9)가 포함 된 개수를 저장 
        tmp = min(X.count(str(i)),Y.count(str(i)))
        # 공통적으로 포함된 개수만큼 answer에 추가
        answer+=tmp*str(i)
        
    #0 처리(결과값과 0의 개수가 같을 경우)
    if len(answer)==answer.count('0') and len(answer)>0:
        answer='0'
    
    #없을 경우 처리
    if len(answer)==0:
        answer='-1'
    
    return answer