def solution(genres, plays):
    answer = []
    music = {}    
    total = {}
    
    for i in range(0, len(plays)):
        g, p = genres[i], plays[i]
        if g not in music:
            music[g] = [[i,p]]
            total[g] = p
        else:
            music[g].append([i,p])
            total[g] += p
    
    total = dict(sorted(total.items(), key = lambda x: x[1], reverse = True))

    for t in total:
        music[t].sort(key = lambda x : x[1], reverse = True)
        
        for i in music[t][0:2]:
            answer.append(i[0])
    
    return answer