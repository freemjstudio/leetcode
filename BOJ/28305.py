# https://www.acmicpc.net/problem/28305 세미나 배정

n, t = map(int, input().split())
array = list(map(int, input().split())) # 반드시 세미나 하는 날 (외부 세미나)
array.sort()  # 3 4 5 6 7
dp = [0] * 200001

