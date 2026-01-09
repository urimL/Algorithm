import heapq

def solution(book_time):
    answer = 0
    
    #청소시간 계산
    def time(time):
        start_h, start_m = map(int,time[0].split(":"))
        end_h, end_m = map(int, time[1].split(":"))
        
        if end_m >= 50:
            end_h += 1
            end_m = end_m + 10 - 60
        else:
            end_m += 10
            
        return [start_h*100 + start_m, end_h*100 + end_m ]

    book_time.sort()
    hq = [9999]
    
    for t in book_time:
        s,e = time(t)
        
        if hq:
            min_endtime = hq[0]
            print(min_endtime)
        
        # new endtime
        if min_endtime > s:
            answer += 1
        else:
            heapq.heappop(hq)
        heapq.heappush(hq,e)   
        
    return answer