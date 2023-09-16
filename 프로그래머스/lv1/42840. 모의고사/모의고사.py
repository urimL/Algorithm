def solution(answers):
    answer = []
    score=[0,0,0]
    
    how1 = [1, 2, 3, 4, 5]
    how2 = [2, 1, 2, 3, 2, 4, 2, 5]
    how3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i]==how1[i%len(how1)]:
            score[0]+=1
        if answers[i]==how2[i%len(how2)]:
            score[1]+=1
        if answers[i]==how3[i%len(how3)]:
            score[2]+=1
            
    max_score = max(score)
    
    for i in range(len(score)):
        if max_score==score[i]:
            answer.append(i+1)
                   
    return answer