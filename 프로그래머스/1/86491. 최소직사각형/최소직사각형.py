def solution(sizes):
    answer = 0
    w,h = [],[]
    for i in sizes:
        if i[0]<i[1]:
            w.append(i[1])
            h.append(i[0])
        else:
            w.append(i[0])
            h.append(i[1])
            
    answer = max(w)*max(h)
    return answer