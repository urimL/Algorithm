def solution(s):
    s = list(s)
    if s[-1] == "(":
        return False
    
    tmp = []
    while s:
        if s[-1] == "(" and tmp:
            tmp.pop()
            s.pop()
        elif s[-1] == ")":
            tmp.append(s.pop())
        else:
            return False
    
    if not tmp and not s:
        return True
    return False