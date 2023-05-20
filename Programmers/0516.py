# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def check(arr, K):
    for i in arr:
        if i < K:
            return False
    return True


def solution(scoville, K):
    answer = 0
    queue = []
    INF = 10000000
    # 초기 힙큐 구성
    for i in scoville:
        heapq.heappush(queue, i)
    # print(heapq)
    while True:
        low1 = heapq.heappop(queue)  # heappop 하면 가장 작은 원소 리턴
        low2 = heapq.heappop(queue)
        mixed = low1 + low2 * 2
        heapq.heappush(queue, i)
        answer += 1  # 섞는 횟수 + 1

        if check(queue, K):
            break
        if answer >= INF:
            break

            # 정답 출력
    if answer >= INF:
        return -1
    else:
        return answer