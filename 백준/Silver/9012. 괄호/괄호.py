import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = input().rstrip()
    st = []
    check = True

    for j in s:
        if j=='(':
            st.append(j)
        else:
            if st and st[-1]=='(':
                st.pop()

            else:
                check = False
                break
            
    if not st and check:
        print('YES')
    else:
        print("NO")
