import sys
input = sys.stdin.readline

n = int(input())
st = [0]
for _ in range(n):
    st.append(int(input()))

dp = [0] * (n+1)
dp[0], dp[1] = st[0], st[0]+st[1]
for i in range(2,n+1):
    dp[i] = max(dp[i-2]+st[i], dp[i-3] + st[i-1] + st[i])
print(dp[-1])