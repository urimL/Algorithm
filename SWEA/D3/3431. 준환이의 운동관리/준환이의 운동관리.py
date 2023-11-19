def solution():
    T = int(input())

    for t in range(1,T+1):
        minvalue,maxvalue,now = map(int,input().split())
        if now<minvalue:
            answer = minvalue-now
        elif now>maxvalue:
            answer = -1
        else:
            answer = 0

        print(f'#{t} {answer}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution()

