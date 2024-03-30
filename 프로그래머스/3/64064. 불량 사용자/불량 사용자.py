from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    result = []
    user_id.sort()
    
    def check(x,y): 
        for i in range(len(y)):
            if len(x[i]) != len(y[i]):
                return False

            for j in range(len(x[i])):
                if y[i][j] == '*':
                    continue
                if y[i][j] != x[i][j]:
                    return False
        return True
            

    p_user = permutations(user_id, len(banned_id))
    result = []
    
    for p in p_user:
        if not check(p, banned_id):
            continue
            
        p = set(p)
        if p not in result:
            result.append(p)
            
    answer = len(result)
    return answer