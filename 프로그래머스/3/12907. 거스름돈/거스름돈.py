def solution(n, money):
    answer = 0
    count = [0] * (n+1)
    count[0] = 1
    
    for m in money:
        for i in range(m, n+1):
            if i >= m:
                count[i] += count[i-m]

    answer = count[n]
    return answer%1000000007