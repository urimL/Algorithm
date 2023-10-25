import sys
from collections import deque
input = sys.stdin.readline

sentence = []

while True:
    i = input().rstrip()
    if i=='.':
        break
    sentence.append(i)

for i in sentence:
    check = True
    st = []
    for j in i:
        if j=='(' or j=='[':
            st.append(j)
            
        elif j==')':
            if not st or st[-1]!='(':
                check = False
                break
            elif st[-1]=='(':
                st.pop()
        elif j==']':
            if not st or st[-1]!='[':
                check = False
                break
            elif st[-1]=='[':
                st.pop()



    if len(st)==0 and check:
        print('yes')
    else:
        print('no')
