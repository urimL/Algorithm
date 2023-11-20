def solution():
    n = int(input())
    m = int(input())
    nums = list(map(int,input().split()))
    start,end = 0,n-1
    answer=0
    nums.sort()

    while start<end:
        now = nums[start]+nums[end]
        if now==m:
            answer+=1
            start+=1
            end-=1
        elif now<m:
            start+=1
        else:
            end-=1

    print(f'{answer}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution()

