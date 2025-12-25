import math

def time_check(start, end):
    s_hour, s_minute = map(int, start.split(":"))
    e_hour, e_minute = map(int, end.split(":"))
    
    # 모든 시간을 '분'으로 환산해서 단순 뺄셈
    start_total = s_hour * 60 + s_minute
    end_total = e_hour * 60 + e_minute
    
    return end_total - start_total

def check(st):
    result = 0
    if len(st) % 2 != 0:
        st.append('23:59')
    
    while st:
        end = st.pop()
        start = st.pop()

        result += time_check(start, end)
 
    return result
        
    
def solution(fees, records):
    answer = []
    res = []
    d = dict()
    
    for r in records:
        t, n, w = r.split(" ")
        if n not in d:
            d[n] = [t]
        else:
            d[n].append(t)
    
    for i in d:
        total = check(d[i])
        answer.append([i, total])
    
    idx = 0
    
    def_time, def_cost, time, cost = fees
    for num, c in answer:
        if c <= def_time:
            res.append([num,def_cost])
        else:
            tmp = def_cost + math.ceil((c - def_time)/time) * cost
            res.append([num, tmp])
    
    res.sort()
    
    return [x[1] for x in res]