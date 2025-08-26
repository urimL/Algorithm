def solution(n, number):
    
    if n == number:
        return 1
        
    
    answer = -1
    check = [set() for _ in range(8)]
    
    for i in range(8):
        check[i].add(int(str(n)*(i+1)))
        
    for i in range(1, 8):
        for j in range(i):
            for op1 in check[j]:
                for op2 in check[i-j-1]:
                    check[i].add(op1+op2)
                    check[i].add(op1*op2)
                    check[i].add(op1-op2)
                    if op2!=0:
                        check[i].add(op1//op2)
        if number in check[i]:
            answer = i+1
            break

    return answer