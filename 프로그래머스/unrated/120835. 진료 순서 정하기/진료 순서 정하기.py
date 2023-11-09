def solution(emergency):
    answer = []
    tmp = []

    for i in emergency:
        tmp.append([i,emergency.index(i)+1])
    
    tmp.sort(reverse=True)
    
    for i in range(len(tmp)):
        tmp[i].append(i+1)
    
    tmp.sort(key=lambda x:x[1])
    for i in tmp:
        answer.append(i[2])

    return answer