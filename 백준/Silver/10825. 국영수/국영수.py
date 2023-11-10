import sys
input = sys.stdin.readline

t = int(input())
st = []
for i in range(t):
    a,b,c,d = list(map(str,input().split()))
    st.append([a,int(b),int(c),int(d)])

st.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in st:
    print(i[0])
