# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    total_weights = 0  # 다리 위에 있는 트럭의 무게
    while bridge:
        total_weights -= bridge.popleft()
        answer += 1
        if truck_weights:
            if truck_weights[0] + total_weights <= weight:
                truck = truck_weights.popleft()
                total_weights += truck
                bridge.append(truck)
            else:
                bridge.append(0)

    return answer