def solution(answers):
    answer = []
    student = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    result = [0,0,0]
    
    for i in range(len(answers)):
        for j in range(len(student)):
            if answers[i] == student[j][i%len(student[j])]:
                result[j] += 1
        
    max_score = max(result)
    for i in range(3):
        if result[i] == max_score:
            answer.append(i+1)
    
    return answer