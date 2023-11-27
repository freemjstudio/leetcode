N = int(input())
data = list(map(int, input().split()))
idx1, idx2 = 0, 0
data.sort() # 정렬하기
value = int(1e9)*2
left, right = 0, N-1
while left < right:
    temp = data[left] + data[right]
    if value > abs(temp):
        value = abs(temp)
        idx1, idx2 = left, right

    if temp < 0:
        left += 1
    else:
        right -= 1


print(data[idx1], data[idx2])