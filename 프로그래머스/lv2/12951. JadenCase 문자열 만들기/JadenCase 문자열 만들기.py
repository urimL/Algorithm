def solution(s):
    answer = ''
    words = s.split(" ")
    result = []
    
    for c in words:
        if c != "":
            result.append(c[0].upper() + c[1:].lower())
        else:
            result.append("")
            
    answer=" ".join(result)
    return answer