def solution(array, commands):
    answer = []
    for c in commands:
        i,j,k = c        
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer