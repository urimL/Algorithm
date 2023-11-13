import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
answer,st = [-1]*n,[]

for i in range(len(num)):
    while st and num[st[-1]]<num[i]:
        answer[st.pop()] = num[i]
    st.append(i)

print(*answer)

