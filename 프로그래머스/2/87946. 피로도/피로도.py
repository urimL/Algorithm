from itertools import permutations

def solution(k, d):
    answer = 0
    d_num = len(d)
    
    for p in permutations(d,d_num):
        cnt = 0
        hp = k
        for i in p:
            if hp>=i[0]:
                hp-=i[1]
                cnt+=1
        if cnt>answer:
            answer=cnt
        
    return answer