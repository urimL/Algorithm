def solution(n, k, cmd):
    dic = {i: [i - 1, i + 1] for i in range(n)}
    deleted = []
    
    for c in cmd:
        if c[0] == 'U':
            x = int(c.split()[1])
            for _ in range(x):
                k = dic[k][0]
                
        elif c[0] == 'D':
            x = int(c.split()[1])
            for _ in range(x):
                k = dic[k][1]
                
        elif c[0] == 'C':
            pre, nxt = dic[k]
            deleted.append((k, pre, nxt))
            if pre != -1:
                dic[pre][1] = nxt
            if nxt != n:
                dic[nxt][0] = pre
            del dic[k]
            k = nxt if nxt != n else pre  # 커서 이동
            
        else:  # Z
            now, pre, nxt = deleted.pop()
            dic[now] = [pre, nxt]
            if pre != -1:
                dic[pre][1] = now
            if nxt != n:
                dic[nxt][0] = now
    
    # 최종 결과 문자열 생성
    answer = ['O'] * n
    for i, _, _ in deleted:
        answer[i] = 'X'
    return ''.join(answer)
