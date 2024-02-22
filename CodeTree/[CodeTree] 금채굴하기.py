n, m = map(int, input().split())
array = []
for _ in range(n): # n * n 영역
    array.append(list(map(int, input().split())))

dx = [1, 1, -1, -1]
dy = [-1, 1, -1, 1] # ->

# k 에 대한 마름모의 넓이
def get_size(k):
    return k * k + (k+1) * (k+1)
# 좌표가 겪자에 표함 되는지 확인
def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False