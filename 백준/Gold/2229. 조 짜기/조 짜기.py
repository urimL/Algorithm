import sys

input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(2, n + 1):
    tmp_max = -1
    for j in range(i - 1, -1, -1):
        tmp_arr = score[j:i]
        tmp_max = max(tmp_max, max(tmp_arr) - min(tmp_arr) + dp[j])

    dp[i] = tmp_max

print(dp[n])
