def solution(numlist, n):
    answer = []
    tmp = []
    
    for i in numlist:
        tmp.append((abs(n-i),-i,numlist.index(i)))
        
    tmp.sort()
    print(tmp)
    
    for i in tmp:
        answer.append(numlist[i[2]])
    return answer