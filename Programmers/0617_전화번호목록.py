# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book)
    for i in range(n-1): # 앞 뒤 비교하기
        if len(phone_book[i]) < len(phone_book[i+1]):
            m = len(phone_book[i])
            if phone_book[i+1][:m] == phone_book[i]:
                answer = False
                return answer
    return answer