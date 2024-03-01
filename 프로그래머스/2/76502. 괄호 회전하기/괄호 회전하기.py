import sys
from collections import deque
input = sys.stdin.readline

def solution(s):
    answer = 0
    q = deque(s)
    
    def check(x):
        st = []
        for i in x:
            if not st or i == "(" or i == "[" or i == "{":
                st.append(i)
            elif i == ")":
                if st and st[-1] == "(":
                    st.pop()
            elif i == "}":
                if st and st[-1] == "{":
                    st.pop()
            else:
                if st and st[-1] == "[":
                    st.pop()
            
        if not st:
            return True
        return False

    for i in range(len(s)):
        q.rotate(-1)
        
        if check(q):
            answer += 1
    
    return answer
                    