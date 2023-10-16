def solution(number, k):
    answer = ''
    st = []
    cnt = 0
    
    for i in range(len(number)):
        if not st or st[-1]>=number[i] or cnt>=k:
            st.append(number[i])
        else:
            while st[-1]<number[i]:
                st.pop()
                cnt+=1
                if not st or cnt==k:
                    break
            st.append(number[i])
    
    if cnt!=k:
        for i in range(k-cnt):
            st.pop()
        

    answer = "".join(st)
    return answer