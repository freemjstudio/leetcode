def solution(clothes):
    answer = 1
    hash_map = {}
    for name, category in clothes:
        hash_map[category] = hash_map.get(category, 0) + 1

    for category in hash_map.keys():
        answer *= (hash_map[category] + 1)

    return answer - 1  # 아무 옷도 입지 않는 경우 제외

'''
경우의 수 개념을 생각하기 
'''