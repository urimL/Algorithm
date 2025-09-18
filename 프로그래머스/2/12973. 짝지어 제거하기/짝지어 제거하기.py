def solution(s):
    answer = -1
    
    st = []
    
    for i in s:
        if not st or st[-1] != i:
            st.append(i)
        elif st and st[-1] == i:
            st.pop()
            continue
        
    if not st:
        return 1
    
    return 0