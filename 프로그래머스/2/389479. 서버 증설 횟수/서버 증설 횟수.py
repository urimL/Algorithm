def solution(players, m, k):
    server=[0]*24
    answer = 0
    
    for idx, p in enumerate(players):
        need = p//m
        if server[idx] < need:
            tmp = need - server[idx]
            answer += tmp
            if idx + k < 24:
                for i in range(idx, idx+k):
                    server[i] += tmp
            else:
                for i in range(idx, 24):
                    server[i] += tmp
        print(server)
    return answer