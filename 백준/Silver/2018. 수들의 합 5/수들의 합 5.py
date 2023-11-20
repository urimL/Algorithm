def solution():
    n = int(input())
    cnt, sum = 0, 0
    start, end = 0, 0

    while end <= n:
        if sum < n:
            end += 1
            sum += end
        elif sum > n:
            sum -= start
            start += 1
        else:
            cnt += 1
            end += 1
            sum += end

    print(f'{cnt}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
