def solution(numbers):
    answer = 0
    alp = {'zero' : 0, 'one':1, 'two':2, 'three' : 3, 'four':4,'five':5,'six' : 6, 'seven' : 7, 'eight':8,'nine':9}
    
    for i,j in alp.items():
        if i in numbers:
            numbers = numbers.replace(i,str(j))
    answer = int("".join(numbers))
    return answer