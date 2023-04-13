# 2141 우체국 https://www.acmicpc.net/problem/2141
import sys

N = int(input())

data = []
people = 0
for _ in range(N):
    x, a = map(int, input().split())
    data.append([x, a])
    people += a

data.sort(key= lambda x:x[0])



