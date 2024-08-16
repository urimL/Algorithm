def solution(elements):
    answer = set()
    l = len(elements)
    
    elements = elements*2
    
    for i in range(1, l + 1):
        for j in range(l):
            s = sum(elements[j:j+i])
            answer.add(s)
    return len(answer)