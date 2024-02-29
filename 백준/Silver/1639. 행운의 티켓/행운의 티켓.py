import sys

input = sys.stdin.readline

ticket = input().rstrip()

answer = 0

for mid in range(1, len(ticket)):
    for cnt in range(1, mid + 1):  # 한 쪽 개수
        cnt = min(cnt, len(ticket) - mid, mid)
        l_total = sum(map(int, ticket[mid - cnt : mid]))
        r_total = sum(map(int, ticket[mid : mid + cnt]))

        if l_total == r_total:
            answer = max(answer, cnt * 2)

print(answer)
