import heapq

def solution(operations):
    answer = []
    h = []

    for i in operations:
        m = i.split()
        tmp = int(m[1])
        if m[0]=="I":
            tmp = int(m[1])
            heapq.heappush(h,tmp)
            
        elif m[0]=="D" and tmp==1:
            if len(h)!=0:
                max_v = max(h)
                h.remove(max_v)
        else:
            if len(h)!=0 :
                heapq.heappop(h)
        
                
    if not h:
        return [0,0]
    else:
        return [max(h),heapq.heappop(h)]
        