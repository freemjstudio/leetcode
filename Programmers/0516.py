# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def check(arr):
    for i in arr:
        if i < k:
            return False
    return True


def solution(scoville, K):
    answer = 0

    while True:

        answer += 1  # 섞는 횟수 + 1

        if check(scoville):
            break

    return answer