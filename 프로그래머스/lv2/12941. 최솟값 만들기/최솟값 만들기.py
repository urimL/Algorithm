def solution(A,B):
    answer = 0

    return sum([a*b for a,b in zip(sorted(A),sorted(B,reverse=True))])
