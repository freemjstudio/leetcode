# 선택 정렬 - 오름차순으로 정렬
# O(N**2)
def selection_sort(arr):
    N = len(arr)
    for i in range(N-1):
        min_idx = i # 확인하려는 인덱스 위치
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]: # 더 작은 값을 발견하면
                min_idx = j # min_idx 를 갱신!
        # swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 삽입 정렬 - 오름차순 정렬
# O(N**2)
def insertion_sort(arr):
    N = len(arr)
    for i in range(1, N): # 정렬 범위를 하나씩 늘려가기
        for j in range(i, 0, -1): # 정렬 범위 내에서 정렬하기
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j], arr[j-1]


def bubble_sort(arr):
    N = len(arr)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

print(bubble_sort([4,7,2,8,1,9,0]))
# Merge Sort