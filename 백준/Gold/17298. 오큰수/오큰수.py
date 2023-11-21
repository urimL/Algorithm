def solution():
    n = int(input())
    nums = list(map(int,input().split()))
    answer = [0]*n
    st = []

    for i in range(n-1,-1,-1):
        if not st:
            answer[i] = -1
            st.append(nums[i])
        else:
            while st:
                if nums[i] < st[-1]:
                    answer[i] = st[-1]
                    st.append(nums[i])
                    break
                st.pop()
            if not st:
                answer[i] = -1
                st.append(nums[i])

    for i in answer:
        print(i,end=' ')

if __name__ == '__main__':
    solution()
