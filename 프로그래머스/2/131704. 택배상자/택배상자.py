def solution(order):
    answer = 0
    st = []
    cnt = 1
    
    while cnt!=len(order)+1:
        st.append(cnt)
        while st and st[-1]==order[answer]:
            answer+=1
            st.pop()
        cnt+=1
    
    return answer