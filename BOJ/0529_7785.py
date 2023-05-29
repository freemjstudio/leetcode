# https://www.acmicpc.net/problem/7785
from collections import defaultdict
# 회사에 있는 사람

d = defaultdict(list)
n = int(input())
for _ in range(n):
    name, command = input().split()
    if len(d[name]) == 0:
        d[name].append(command) # 회사에 출입
    else:
        if command == "leave":
            # key 삭제
            d.pop(name, None) # dictionary 에 Key값이 없으면 None을 리턴한다.

answer = sorted(d.keys(), reverse=True)
for name in answer:
    print(name)