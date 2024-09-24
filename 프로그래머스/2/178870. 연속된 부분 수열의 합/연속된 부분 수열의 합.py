def solution(sequence, k):
    answer = []
    start, end, s = 0, 0, sequence[0]
    
    while start <= end:
        if s == k:
            answer.append([start, end])
            s -= sequence[start]
            start += 1
        elif s < k:
            end += 1
            if end >= len(sequence):
                break
            s += sequence[end]
        else:
            s -= sequence[start]
            start += 1
        
    answer.sort(key = lambda x:x[1]-x[0])
    return answer[0]