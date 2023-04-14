# 2141 우체국 https://www.acmicpc.net/problem/2141
import sys
input = sys.stdin.readline
N = int(input())

data = []
total_people = 0
for _ in range(N):
    x, a = map(int, input().split())
    data.append([x, a])
    total_people += a

data.sort()

count = 0
for i in range(N):
    t, p = data[i]
    count += p
    if count >= total_people/2: # 마을 사람 수가 절반이 넘어가는 그 마을이 정답
        print(t)
        break

# 사람 수만 따져도 가능한 이유는 -> N개의 마을 간격이 일정하기 때문이다 !