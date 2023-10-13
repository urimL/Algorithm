def solution(genres, plays):
    answer = []
    total = {}
    g_play = {}
    
    for i in range(len(plays)):
        if genres[i] in total.keys():
            total[genres[i]]+=plays[i]
            g_play[genres[i]].append((plays[i],i))
        else:
            total[genres[i]] = plays[i]
            g_play[genres[i]] = [(plays[i],i)]
    
    total = sorted(total.items(), key=lambda x:x[1],reverse=True)
    
    for k in total:
        playlist = g_play[k[0]]
        playlist = sorted(playlist,key=lambda x:x[0],reverse=True)
        
        for i in range(len(playlist)):
            if i==2:
                break
            answer.append(playlist[i][1])
    
    return answer