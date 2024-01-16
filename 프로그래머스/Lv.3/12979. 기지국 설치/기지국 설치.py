import math
def solution(n, stations, w):
    answer = 0
    start =1
    stations.append(n+w+1)
    for s in stations:
        cnt = s-w-start
        
        if cnt%(w*2+1)==0:
            answer+=cnt//(w*2+1)
        else:
            answer+=cnt//(w*2+1)+1

        start = s+w+1
    
    return answer