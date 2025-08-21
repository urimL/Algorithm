def solution(number, k):
    num = list(map(int, list(number))) 
    total = len(num)
    st = []
    cnt = 0
    
    for n in num:
        cnt += 1
        while st and st[-1] < n and k > 0:
            st.pop()
            k -= 1
        if k + len(st) == total and cnt == total:
            break
        st.append(n)
       
    answer = "".join(list(map(str, list(st))))
    return answer