import sys
input = sys.stdin.readline

n = int(input())
building,st = [],[]
answer=0

for i in range(n):
    building.append(int(input()))

for i in building:
    while st and st[-1]<=i:
        st.pop()
    answer+=len(st)
    st.append(i)
    
        
print(answer)
