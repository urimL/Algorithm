def solution(answers):
    answer = []
    student = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    score = []
    for s in student:
        count = 0
        for i in range(len(answers)):
            length = len(s)
            if answers[i] == s[i%length]:
                count += 1
        
        score.append(count)
    
    max_score = max(score)
    for i in range(3):
        if max_score == score[i]:
            answer.append(i+1)
    return answer