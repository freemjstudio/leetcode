# https://www.acmicpc.net/problem/2304
N = int(input()) # 기둥 개수
answer = 0

stack = []
bars = []
max_length = 0 # 가로축 위치
max_height = 0
max_height_index = 0

for _ in range(N):
    L, H = map(int, input().split())
    bars.append([L, H])
    max_length = max(L, max_length)
    if max_height < H:
        max_height = H # 분기점
        max_height_index = L

data = [0] * 1001 # N 1 ~ 1000
for l, h in bars:
    data[l] = h

now_max_height = 0 # 지금까지 등장한 height 중 가장 큰 height
# left -> right
for i in range(max_height_index+1):
    h = data[i]
    if h > now_max_height:
        now_max_height = h
    answer += now_max_height
temp1 = answer
now_max_height = 0
# left <- right
for j in range(max_length, max_height_index, -1):
    h = data[j]
    if h > now_max_height:
        now_max_height = h
    answer += now_max_height

print(answer)
