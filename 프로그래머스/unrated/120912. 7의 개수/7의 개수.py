def solution(array):
    answer=0
    for i in array:
        tmp = str(i)
        answer+=tmp.count('7')
    return answer