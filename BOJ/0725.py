# https://www.acmicpc.net/problem/3020

n, h = map(int, input().split()) # 구간의 개수 h 개
array = []

min_value = n # 장애물 최솟값
count = 0

up = []
down = []

for i in range(n):
    if i % 2 == 1: # down
        down.append(int(input()))
    else: # up
        up.append(int(input()))

for i in range(h):


print(min_value, count)
