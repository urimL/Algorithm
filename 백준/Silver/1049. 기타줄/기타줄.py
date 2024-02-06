import sys
import math

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())

    if n <= 6:
        now = 1001
        for _ in range(m):
            s, o = map(int, input().split())
            now = min(s, o * n, now)
        return now

    else:
        s_now = 1001
        o_now = 1001
        for _ in range(m):
            s, o = map(int, input().split())
            s_now = min(s_now, s, o * 6)
            o_now = min(o_now, o)

        mix_total = n // 6 * s_now + (n % 6) * o_now
        set_total = math.ceil(n/6) * s_now
        one_total = o_now * n

        return min(mix_total, set_total, one_total)


print(solution())
