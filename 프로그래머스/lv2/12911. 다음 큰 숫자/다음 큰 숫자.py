def solution(n):
    answer = 0
    bn = bin(n)
    cnt = str(bn).count("1")
    
    while True:
        n+=1
        tmp = bin(n)
        if cnt == str(tmp).count("1"):
            answer = int(n)
            break
    return answer
