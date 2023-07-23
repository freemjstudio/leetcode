# 강의실 배정 https://www.acmicpc.net/problem/11000
import heapq

N = int(input())

time = []

for _ in range(N):
    S, T = map(int, input().split())
    time.append((S, T))

time.sort()
queue = []

heapq.heappush(queue, time[0][1]) # 수업 끝나는 시간 ex, (1, 3) 에서 3
for i in range(1, N):
    if time[i][0] >= queue[0]: # 회의실 추가 필요 없음
        heapq.heappop(queue)
        heapq.heappush(queue, time[i][1])
    else: # 회의실 추가 필요함
        heapq.heappush(queue, time[i][1])
print(len(queue))
