def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        if i**2 > yellow:
            break
        if yellow % i != 0:
            continue
        else:
            x,y = i, yellow//i
            cnt = x*2 + y*2 + 4
            if cnt == brown:
                return [y+2, x+2]

    return answer