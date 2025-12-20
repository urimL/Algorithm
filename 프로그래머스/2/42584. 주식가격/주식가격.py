from collections import deque

def solution(prices):
    answer = [0 for _ in range(len(prices))] 
    q = deque() 
    new_prices = []
    for i in range(len(prices)):
        new_prices.append([i, prices[i]])
    
    for p in new_prices:
        while q and q[-1][1] > p[1]:
            answer[q[-1][0]] = p[0] - q[-1][0]
            q.pop()
        else:
            q.append(p)
    
    while q:
        answer[q[0][0]] = len(prices) - q[0][0]-1
        q.popleft()
    
    return answer