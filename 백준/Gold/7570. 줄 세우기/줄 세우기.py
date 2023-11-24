import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
result = 0
dp = [0]*(n+1)

for i in nums:
    dp[i] = dp[i-1]+1
    result = max(result,dp[i])
    
print(n-result)