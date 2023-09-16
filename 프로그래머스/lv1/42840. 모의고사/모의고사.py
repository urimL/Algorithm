def solution(answers):
    answer = []
    score1,score2,score3 = 0,0,0
    
    how1 = [1, 2, 3, 4, 5]
    how2 = [2, 1, 2, 3, 2, 4, 2, 5]
    how3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i]==how1[i%len(how1)]:
            score1+=1
        if answers[i]==how2[i%len(how2)]:
            score2+=1
        if answers[i]==how3[i%len(how3)]:
            score3+=1
            
    max_score = max(score1,score2,score3)
            
    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)
           
    return answer