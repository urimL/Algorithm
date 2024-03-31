def solution(sequence):
    length = len(sequence)
    pulse = lambda x : 1 if x % 2 else -1
    sequence = [ pulse(idx) * sequence[idx] for idx in range(length) ]
    
    dp = [[0, 0] for _ in range(length)]
    dp[0] = [sequence[0], sequence[0]]

    for i in range(1, length) :
        num = sequence[i]
        dp[i][0] = min(num, num + dp[i-1][0])
        dp[i][1] = max(num, num + dp[i-1][1])

    min_val = min(map(min, dp))
    max_val = max(map(max, dp))
        
    return max(abs(min_val), abs(max_val))
