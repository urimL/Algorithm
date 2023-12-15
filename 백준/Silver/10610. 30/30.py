import sys

input = sys.stdin.readline

st = list(input().rstrip())
st.sort(reverse=True)
now = 0

if '0' not in st:
    print(-1)
else:
    for i in st:
        now += int(i)

    if now%3 != 0:
        print(-1)
    else:
        num = sorted(st, reverse=True)
        answer = "".join(num)
        print(answer)
