from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    st = []
    
    for i in range(len(speeds)-1, -1, -1):
        st.append([i, math.ceil((100-progresses[i])/speeds[i])])
        
    remains = 101
    while st:
        cnt = 0
        remains = st[-1][1]
        while st and st[-1][1] <= remains:
            st.pop()
            cnt += 1
        answer.append(cnt)

    return answer