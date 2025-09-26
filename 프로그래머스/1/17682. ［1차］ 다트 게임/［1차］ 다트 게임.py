def solution(dartResult):
    answer = 0
    score = []
    now = ''
    
    for d in dartResult:
        if d == 'S':
            score.append(int(now))
            now = ''
        elif d == 'D':
            now = str(int(now)**2)
            score.append(int(now))
            now = ''
        elif d == 'T':
            now = str(int(now)**3)
            score.append(int(now))
            now = ''
        elif d == '*':
            if len(score) == 1:
                score[0] *= 2
                continue
            for i in range(len(score)-1, len(score)-3,-1):
                score[i] *= 2
            now = ''
        elif d == '#':
            score[-1] = (-1)*score[-1]
            now = ''
        else:
            now += d
        print(score)
    return sum(score)