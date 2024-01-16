# https://school.programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)

    while queue:
        price = queue.popleft()
        count = 0
        for q in queue:
            count += 1
            if q < price:  # r감소
                break
        answer.append(count)
    return answer

'''
def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                continue

    return answer
'''