def solution(A, B):
    
    def binarySearch(x):
        start, end = 0, len(B)-1
        idx = -1
        
        while start <= end:
            mid = (start+end)//2
            
            if B[mid] <= x:
                start = mid+1
            else:
                idx = mid
                end = mid-1

        return idx
        
    answer = 0
    B.sort()
    visited = [False] * len(B)
    
    for i in A:
        now = binarySearch(i)
        
        while visited[now] and now < len(B)-1:
            now += 1

        if not visited[now] and B[now] > i:
            answer += 1
            visited[now] = True
        
    return answer