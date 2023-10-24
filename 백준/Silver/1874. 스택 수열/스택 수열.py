import sys
input = sys.stdin.readline

n = int(input())
result,st = [],[]
check = True
pos = 1

for i in range(n):
    num = int(input())
    
    while pos<=num:
        st.append(pos)
        pos+=1
        result.append("+")
    if st[-1]==num:
        st.pop()
        result.append('-')
    else:
        check = False
        break

if check:
    for i in result:
        print(i)

else:
    print("NO")
            
