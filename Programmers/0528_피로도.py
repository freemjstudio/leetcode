# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    answer = -1  # 최대 탐험할 수 있는 던전 수
    n = len(dungeons)

    permu = permutations(dungeons, n)

    for p in permu:
        total_k = k
        visit = 0
        # a : 최소 필요 피로도, b : 소모 피로도
        for a, b in p:
            if total_k >= a:
                total_k -= b
                visit += 1
            else:
                break

        answer = max(visit, answer)  # 최댓값 갱신

    return answer