def solution(i, j, k):
    answer = 0
    
    for n in range(i,j+1):
        n=list(str(n))
        answer+=n.count(str(k))
    return answer