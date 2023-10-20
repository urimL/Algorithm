import sys
input = sys.stdin.readline

n = int(input())
st = []
for i in range(n):
    c = list(input().split())
    if c[0]=='push':
        st.append(int(c[1]))
    elif c[0]=='pop':
        if len(st)==0:
            print("-1")
        else:
            print(st.pop())
    elif c[0]=='size':
        print(len(st))
    elif c[0]=='empty':
        if st:
            print(0)
        else:
            print(1)
    else:
        if not st:
            print(-1)
        else:
           print(st[-1])
