def solution(s):
    answer = len(s)
    n = len(s)//2

    for i in range(1, n + 1):
        result = ''
        prev = s[:i]
        count = 1
        
        for j in range(i, len(s), i):
            if prev == s[j:j+i]:
                count += 1
            else:
                result += str(count) + prev if count >= 2 else prev
                prev = s[j:j+i]
                count = 1
        result += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(result))
  
    return answer