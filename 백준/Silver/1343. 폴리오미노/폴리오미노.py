import sys

input = sys.stdin.readline

board = list(input().rstrip())
board.append(".")

answer = []
A = "AAAA"
B = "BB"

count = 0
for b in board:
    if b == ".":
        if count != 0 and count % 2 != 0:
            answer.append(-1)
            break
        elif count != 0 and count % 2 == 0:
            while count > 0:
                if count >= 4:
                    answer.append(A)
                    count -= 4
                elif count >= 2:
                    answer.append(B)
                    count -= 2

        answer.append(b)

    else:
        count += 1

if answer[-1] != -1:
    answer.pop()
    print("".join(answer))
else:
    print(-1)
