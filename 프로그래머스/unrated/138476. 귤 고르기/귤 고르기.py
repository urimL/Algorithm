import collections

def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for i in sorted(cnt.values(), reverse = True):
        k -= i
        answer += 1
        if k <= 0:
            break
    return answer