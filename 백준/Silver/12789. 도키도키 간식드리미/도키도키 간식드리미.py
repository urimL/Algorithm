import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
st = []
now = 1

for i in num:
    if now == i:
        now += 1
        while st and st[-1] == now:
            st.pop()
            now += 1
    else:
        st.append(i)

if not st:
    print('Nice')
else:
    print('Sad')