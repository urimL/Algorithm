def solution():
    s, p = map(int, input().split())
    dna = input()
    cnt = list(map(int, input().split()))
    dic = {'A':cnt[0],'C':cnt[1],'G':cnt[2],'T':cnt[3]}
    base = {'A':0,'C':0,'G':0,'T':0}
    answer = 0

    for i in range(s-p+1):
        ch = True
        if i==0:
            for j in range(p):
                base[dna[j]] += 1
        else:
            base[dna[i+p-1]]+=1
            base[dna[i-1]]-=1

        for m in ('A','C','G','T'):
            if base[m] < dic[m]:
                ch = False
                break

        if ch:
            answer+=1

    print(f'{answer}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution()
