import sys

input = sys.stdin.readline

n = int(input())
card = list(map(int,input().split()))
dp = [0]*(n+1)
dp[1],dp[2] = card[0],max(card[1],card[0]*2)

for i in range(3,n+1):
    max_value = 0
    for j in range(1,i+1):
        if j==1:
            max_value = max(max_value,dp[1]*i)
        else:
            max_value = max(max_value,card[j-1]+dp[i-j])
    dp[i] = max_value

print(dp[n])