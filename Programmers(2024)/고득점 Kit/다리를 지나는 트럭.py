# https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = [0 for _ in range(bridge_length)]
    while bridge:
        bridge.pop(0)
        answer += 1
        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
            else:
                bridge.append(0)

    return answer