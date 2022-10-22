def solution(phone_book):
    hash_book = dict()
    for i in phone_book:
        hash_book[i] = 1
    for i in phone_book:
        tmp = ''
        for j in i:
            tmp = tmp + j
            if tmp in hash_book and tmp != i:
                return False
    return True
