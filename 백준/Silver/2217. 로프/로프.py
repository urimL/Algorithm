def solution(n):
    tmp = []
    for _ in range(n):
        tmp.append(int(input()))


    tmp.sort(reverse=True)
    result = []

    for i in range(n):
        result.append(tmp[i]*(i+1))
        
     
    return max(result)
            

n = int(input())
print(solution(n))
