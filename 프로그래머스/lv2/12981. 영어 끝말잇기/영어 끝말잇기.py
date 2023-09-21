def solution(n, words):
    #실패 : 다른 글자로 시작 or 같은 단어
    #실패시 반환 : 차례와 해당 차례의 사람이 말한 순서 (i+1//n)
    answer = [0,0]
    tmp = [words[0]]
    cnt = 1
    
    for i in range(1,len(words)):
        cnt = i%n+1
        
        if (words[i] in tmp) or (words[i-1][-1] != words[i][0]):
            answer = [cnt,i//n+1]
            print(cnt,i,n)
            break
            
        else:
            tmp.append(words[i])

    return answer