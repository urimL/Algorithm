from itertools import permutations
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**1/2 + 1)):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        perm = permutations(numbers,i)
    
        for c in perm:
            result = int("".join(c))
            if isPrime(result):
                answer.add(result)
    print(answer)
    return len(answer)