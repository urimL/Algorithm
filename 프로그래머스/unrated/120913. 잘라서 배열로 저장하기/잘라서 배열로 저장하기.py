def solution(my_str, n):
    answer = []
    num = len(my_str)/n
    
    for i in range(0,len(my_str),n):
        tmp = "".join(my_str[i:i+n])
        answer.append(tmp)
    return answer