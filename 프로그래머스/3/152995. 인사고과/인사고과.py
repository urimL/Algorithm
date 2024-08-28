def solution(scores):
    answer = 1
    a,b = scores[0]
    total = a+b
    max_a, max_b = 0,0

    scores.sort(key = lambda x:(-x[0], x[1]))

    for i,j in scores:
        if a < i and b < j:
            return -1
        if max_b <= j:
            max_b = j
            if total < i+j:
                answer+= 1
    return answer