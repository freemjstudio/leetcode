# https://school.programmers.co.kr/learn/courses/30/lessons/42584

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