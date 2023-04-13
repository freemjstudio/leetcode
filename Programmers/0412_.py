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

data.sort(key= lambda x:x[0])

count = 0
for i in range(N):
    t, p = data[i]
    count += p
    if count >= total_people/2: # 마을 사람 수가 절반이 넘어가는 그 마을이 정답
        print(t)
        break

