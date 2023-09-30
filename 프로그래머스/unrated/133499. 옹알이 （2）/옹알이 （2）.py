def solution(babbling):
    answer = 0
    ch = True
    can = ["aya", "ye", "woo", "ma"]
    tmp = []
    
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,'#')
        if len(i)==i.count('#'):
            answer+=1


    return answer