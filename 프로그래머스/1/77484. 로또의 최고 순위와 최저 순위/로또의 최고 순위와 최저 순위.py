def solution(lottos, win_nums):
    unknown = 0
    correct = 0
    rank = [6,6,5,4,3,2,1]
    
    for l in lottos:
        if l == 0:
            unknown += 1
            continue
        if l in win_nums:
            correct += 1
    
    answer = [rank[correct+unknown],rank[correct]]
    
    return answer