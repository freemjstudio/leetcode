
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2 # Divide - 비슷한 유형의 더 작은 하위 문제로 분할
    low_arr = merge_sort(arr[:mid]) # 재귀적으로 호출
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0

    # Merge - merge 하면서 정렬이 일어난다.
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]: # 작은 값을 먼저 append 하여 오름차순 정렬 진행
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    # 남은 원소 더해주기
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

'''
분할 정복은 top-down 방식으로 재귀 호출의 장단점과 동일함. 

장점 : top-down 이므로 직관적인 코드 , 문제를 나눠서 해결, 병렬적 해결  
단점 : 재귀 함수 호출로 오버헤드 발생. 
'''

print(merge_sort([5,3,7,2,9,1]))