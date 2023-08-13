# https://school.programmers.co.kr/learn/courses/30/lessons/42746

from itertools import permutations

''' 
시간 초과 ~~~ 

def solution(numbers):
    answer = ''
    n = len(numbers)

    for per in permutations(numbers, n):
        new_num = ''.join(map(str, per))
        answer = max(answer, new_num)
    return answer

'''

'''
from collections import defaultdict


def solution(numbers):
    answer = ''
    n = len(numbers)

    num_dict = defaultdict(int)  # (key) 길이 4 : (value) 원래 숫자값
    same_length_num = []  # 길이를 모두 4로 통일 하기
    max_length = 0
    for num in numbers:
        max_length = max(len(str(num)), max_length)
    for num in numbers:
        l = len(str(num))
        if l == max_length:
            num_dict[num] = num
            same_length_num.append(num)
        elif l < max_length:
            str_num = str(num) + '0' * (4 - max_length)
            num_dict[int(str_num)] = num
            same_length_num.append(int(str_num))
    same_length_num.sort(reverse=True)

    print(same_length_num)
    # 정렬 후 원래 숫자만 가져오기
    for s_num in same_length_num:
        answer += str(num_dict[s_num])

    return answer
'''

def solution(numbers):
    answer = ''
    strnum = list(map(str, numbers))
    same_length = [[i, i * (12 // len(i))] for i in strnum]
    same_length.sort(key=lambda x: x[1], reverse=True)
    for x in same_length:
        answer += x[0]  # original num

    answer = str(int(answer))  # 00 -> 0 예외 처리
    return answer