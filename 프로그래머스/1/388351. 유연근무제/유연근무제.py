#time에 n분을 더한 값 return
def timeCheck(time, n):
    hour, minute = time//100, time%100
    if minute >= 50:
        hour += 1
        minute = minute + n - 60
        return hour * 100 + minute
    else:
        return time + 10
    
def solution(schedules, timelogs, startday):
    answer = 0
    
    for s, times in zip(schedules, timelogs):
        today = startday - 1
        flag = True
        
        #희망 출근 시간
        s = timeCheck(s, 10)
    
        #출근 성공 여부 체크
        for t in times:
            flag = True
            
            #주말 체크
            if today == 5 or today == 6:
                today = (today+1) % 7
                continue
            
            today = (today+1) % 7
            if s >= t:
                continue
            if s < t:
                flag = False
                break
        if flag:
            answer += 1 
    
    return answer