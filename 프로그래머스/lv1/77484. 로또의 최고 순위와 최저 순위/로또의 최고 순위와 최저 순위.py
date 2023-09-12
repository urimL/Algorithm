def solution(lottos, win_nums):
    answer = []
    base_score = 0
    
    for i in lottos:
        if i in win_nums:
            base_score += 1
    
    max_rank = 7-(base_score+lottos.count(0))
    min_rank = 7-base_score
    
    if max_rank>6:
        max_rank=6
    if min_rank>6:
        min_rank=6
    
    
    answer.append(max_rank)
    answer.append(min_rank)
    
    return answer