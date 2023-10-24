import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = list(input().rstrip())
    left,right = [],[]

    for j in range(len(s)):
        if s[j]=='<':
            if left:
                right.append(left.pop())
        elif s[j]=='>':
            if right:
                left.append(right.pop())
        elif s[j]=='-':
            if left:
                left.pop()
        else:
            left.append(s[j])

    left.extend(reversed(right))
    answer = "".join(left)
    print(answer)
    
