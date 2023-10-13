def solution(clothes):
    answer = 0
    cnt = 1
    total = {}
    
    for i in clothes:
        if i[1] in total.keys():
            total[i[1]].append(i[0])
        else:
            total[i[1]] = [i[0]]
    
    for i in total.keys():
        cnt*=(len(total[i])+1)
    
    answer+=cnt
    answer-=1
        
    return answer