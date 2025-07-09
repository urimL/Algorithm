from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    st = []
    for i in range(len(prices)):
        if not st or st[-1][0] <= prices[i]:
            st.append([prices[i], i])
        else:
            while st and st[-1][0] > prices[i]:
                now = st.pop()
                answer[now[1]] += i - now[1]
            st.append([prices[i],i])
        
    cnt = 0
    print(st)
    while st:
        total = len(prices) - 1
        now = st.pop()
        answer[now[1]] += total - now[1]
        
    return answer