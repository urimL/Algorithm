def solution(prices):
    answer = [0 for _ in range(len(prices))] 
    st = []
    
    for i, price in enumerate(prices):
        while st and prices[st[-1]] > price:
            now = st.pop()
            answer[now] = i - now
        st.append(i)
    
    n = len(prices)
    while st:
        now = st.pop()
        answer[now] = n - 1 - now
  
    return answer