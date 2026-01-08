def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    st, num = [], []
 
    for idx, n in enumerate(numbers):
        if not st:
            st.append([idx,n])
            continue
        while st and st[-1][1] < n:
            now = st.pop()
            answer[now[0]] = n
        st.append([idx,n])

    return answer