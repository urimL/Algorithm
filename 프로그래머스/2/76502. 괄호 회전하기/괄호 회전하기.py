from collections import deque

def find(x):
    x = list(x)
    match = {']':'[', ')':'(', '}':'{'}
    tmp = []
    
    while x:
        now = x.pop()
        
        if now == ']' or now == ')' or now == '}':
            if x and x[-1] == match[now]:
                x.pop()
            else:
                tmp.append(now)
        else:
            if tmp and now == match[tmp[-1]]:
                tmp.pop()
            else:
                return False
    if not tmp and not x:
        return True
    return False
    
def solution(s):
    answer = 0

    for i in range(len(s)):
        q = deque(s)
        q.rotate(-i)
        now = "".join(q)
        
        if find(now):
            answer += 1        
        
    return answer