def solution(phone_book):
    phone_book.sort(reverse=False)
    answer = True
    # phone_num = phone_book[0]
    # phone_book_set = set([s[:i]phone_num)
    # for phone in phone_book:
    for i in range(0, len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
            
    return answer