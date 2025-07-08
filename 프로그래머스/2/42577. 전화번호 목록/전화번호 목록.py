def solution(phone_book):
    answer = True
    phone_book.sort()
    dic = dict()
    
    for p, t in zip(phone_book, phone_book[1:]):
        if t.startswith(p):
            return False
    return answer
