from collections import Counter

def solution(topping):
    answer = 0
    #초기 세팅 : 철수가 모두 가진 상황
    chulsu = Counter(topping)
    brother = set()
    
    for t in topping:
        chulsu[t] -= 1
        brother.add(t)
        
        if chulsu[t] == 0:
            chulsu.pop(t)
        if len(chulsu) == len(brother):
            answer += 1

    return answer