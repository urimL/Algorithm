def solution(gems):
    answer = [0, len(gems)]
    gem_list = {gems[0]:1}
    size = len(set(gems))

    start, end = 0,0
    while start < len(gems) and end < len(gems):
        if len(gem_list) == size:
            if answer[1] - answer[0] > end - start:
                answer = [start, end]
            else:
                gem_list[gems[start]] -= 1
                if gem_list[gems[start]] == 0:
                    del gem_list[gems[start]]
                start += 1
                
        else:
            end += 1
            
            if end >= len(gems):
                break
                
            if gems[end] not in gem_list:
                gem_list[gems[end]] = 1
            else:
                gem_list[gems[end]] += 1
                

    return [answer[0]+1, answer[1]+1]