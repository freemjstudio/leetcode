# https://school.programmers.co.kr/learn/courses/30/lessons/42746

from itertools import permutations

from itertools import permutations


def solution(numbers):
    answer = ''
    n = len(numbers)

    for per in permutations(numbers, n):
        new_num = ''.join(map(str, per))
        answer = max(answer, new_num)
    return answer