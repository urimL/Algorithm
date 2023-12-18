import sys
input = sys.stdin.readline

st = input().rstrip()
c = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in c:
    if i in st:
        st = st.replace(i,'*')

print(len(st))
