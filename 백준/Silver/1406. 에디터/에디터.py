import sys
input = sys.stdin.readline

#pos를 기준으로 left,right 스택에 각각 담아준다.
left,right = list(input().rstrip()),[]

for i in range(int(input())):
    command = list(input().rstrip().split())
    if command[0]=='P':
        left.append(command[1])
    elif command[0]=='L' and left:
        right.append(left.pop())
    elif command[0]=='D' and right:
        left.append(right.pop())
    elif command[0]=='B' and left:
        left.pop()

print("".join(left+list(reversed(right))))
