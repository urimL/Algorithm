def solution(cloth):
    answer = 1
    clothes = dict()
    
    for n,c in cloth:
        if c not in clothes:
            clothes[c] = [n]
        else:
            clothes[c].append(n)
    
    total_cnt = len(clothes)
    for c in clothes:
        tmp = len(clothes[c])
        if total_cnt == 1:
            return tmp
        answer *= tmp + 1
    
    return answer - 1