import sys

input = sys.stdin.readline

s = input().rstrip()
st = []
answer = ""
tag = False

for i in s:
    if tag:
        answer += i
        if i == ">":
            tag = False
    else:
        if i == "<":
            while st:
                answer += st.pop()
            tag = True
            answer += i
        elif i == " ":
            while st:
                answer += st.pop()
            answer += i
        else:
            st.append(i)

while st:
    answer += st.pop()
    
print(answer)
