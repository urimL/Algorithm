import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = [1] * (n+1)

for i in range(n):
    for j in range(i+1, n):
        if nums[i] > nums[j]:
            dp[j] = max(dp[i]+1, dp[j])

print(max(dp))