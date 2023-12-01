import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
maxvalue, minvalue = -int(1e9), int(1e9)


def dfs(add, sub, mul, div, idx, num):
    global maxvalue, minvalue
    if idx == n:
        maxvalue = max(maxvalue, num)
        minvalue = min(minvalue, num)
        return

    if add:
        dfs(add - 1, sub, mul, div, idx + 1, num + nums[idx])
    if sub:
        dfs(add, sub - 1, mul, div, idx + 1, num - nums[idx])
    if mul:
        dfs(add, sub, mul - 1, div, idx + 1, num * nums[idx])
    if div:
        dfs(add, sub, mul, div - 1, idx + 1, int(num / nums[idx]))


dfs(add, sub, mul, div, 1, nums[0])

print(maxvalue)
print(minvalue)
