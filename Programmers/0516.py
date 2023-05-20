# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    answer = 0
    queue = []

    # 초기 힙큐 구성
    for i in scoville:
        heapq.heappush(queue, i)

    while queue[0] < K:

        heapq.heappush(queue, heapq.heappop(queue) + heapq.heappop(queue) * 2)

        answer += 1  # 섞는 횟수 + 1

        # 예외 처리 K 이상이 안되는 경우
        if len(queue) == 1 and queue[0] < K:
            return -1
    return answer