# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    answer = 1  # 첫번째 수행 count
    queue = deque(priorities)
    idx = location  # process의 위치를 저장

    while True:
        now = queue.popleft()
        if now < max(queue):  # 더 우선순위가 높은 것이 있을 떄
            queue.append(now)
            if idx == 0:  # 자기 자신인 경우
                idx = len(queue) - 1  # 다시 맨 뒤로 보냄
            else:  # 1이상인 경우
                idx -= 1

        else:  # now 가 가장 높을 때
            if idx == 0:  # now 가 location이 가리키는 값일 때
                return answer
            else:
                answer += 1
                idx -= 1  # location 을 한칸 앞으로 땡긴다

    return answer