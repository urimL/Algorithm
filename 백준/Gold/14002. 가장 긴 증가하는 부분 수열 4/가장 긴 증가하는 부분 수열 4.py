import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n
max_value = 0
max_dp = []

for i in range(n):
    tmp = []
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[j]+1, dp[i])

result = []
pos = max(dp)

for i in range(n-1,-1,-1):
    if dp[i] == pos:
        result.append(nums[i])
        pos -= 1

print(max(dp))
result.reverse()
print(*result)
